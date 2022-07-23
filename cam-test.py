import cv2
import argparse
import time
from otsu_binarization import compute_otsu_binarization, grayConversion
from motion_control import move_forward, probe_check_forward,probe_check_right, stop_forward, move_backward, stop_backward, move_left, stop_left, move_right, stop_right, stop_car

capture = cv2.VideoCapture(1)

if (capture.isOpened() == False):
    print("Error opening video stream!")

parser = argparse.ArgumentParser()
parser.add_argument("--record",action="store_true")
args=parser.parse_args()

successful = True
recording = args.record
print(f"Record: {recording}")

start_time = time.time()
counter = 0
threshold = 0

frame_width = int(capture.get(3))
frame_height = int(capture.get(4))

out = cv2.VideoWriter('output.av', cv2.VideoWriter_fourcc(
    'M', 'J', 'P', 'G'), 30, (frame_width, frame_height))

cv2.namedWindow("preview", cv2.WINDOW_NORMAL)
while successful:
    counter += 1

    successful, image = capture.read()
    if cv2.waitKey(1) & 0xFF == ord('r'):
        print('Recording...')
        recording = True

    img = grayConversion(image)
    # cv2.imshow("Gray Image", img)
    # Compute otsu binarization for each frame
    # threshholded_im_mine = compute_otsu_binarization(img)

    # OpenCV Otsu
    ret, threshholded_im = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                                         cv2.THRESH_OTSU)
    # cv2.imshow("Otsu Binarization(CV)", threshholded_im)
    # cv2.imshow("Otsu Binarization(Mine)", threshholded_im_mine)
    # cv2.imshow("preview", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quitting...')
        break
    if recording:
        out.write(threshholded_im)

    can_go_forward=probe_check_forward(threshholded_im)
    can_go_right=probe_check_right(threshholded_im)
    cv2.imshow("Probes",threshholded_im)

    # Main motor control
    if can_go_forward:
        print("Going forward..." )
        move_forward()
    elif can_go_right:
        print("Going right..." )
        move_left()
    else:
        print("Stopping car...")
        stop_car()

# stop_car()
finish_time = time.time()
fps = counter / (finish_time-start_time)
print('Frames per second: ' + str(fps))
capture.release()
out.release()
cv2.destroyAllWindows()
