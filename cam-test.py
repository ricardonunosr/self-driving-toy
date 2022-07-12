import cv2
import time
from otsu_binarization import compute_otsu_binarization, grayConversion
import numpy as np

capture = cv2.VideoCapture(1)

if (capture.isOpened() == False):
    print("Error opening video stream!")

successful = True
recording = False

start_time = time.time()
counter = 0
threshold = 0

frame_width = int(capture.get(3))
frame_height = int(capture.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(
    'M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

cv2.namedWindow("preview", cv2.WINDOW_NORMAL)
while successful:
    counter += 1

    successful, image = capture.read()
    if cv2.waitKey(1) & 0xFF == ord('r'):
        print('Recording...')
        recording = True
    if recording:
        out.write(image)

    img = grayConversion(image)
    cv2.imshow("Gray Image", img)
    # Compute otsu binarization for each frame
    threshholded_im_mine = compute_otsu_binarization(img)

    ret, threshholded_im = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                                         cv2.THRESH_OTSU)
    cv2.imshow("Otsu Binarization(CV)", threshholded_im)
    cv2.imshow("Otsu Binarization(Mine)", threshholded_im_mine)
    cv2.imshow("preview", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quitting...')
        break

finish_time = time.time()
fps = counter / (finish_time-start_time)
print('Frames per second: ' + str(fps))
capture.release()
out.release()
cv2.destroyAllWindows()
