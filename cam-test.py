import cv2
import time

capture = cv2.VideoCapture(1)

if (capture.isOpened() == False):
    print("Error opening video stream!")

successful = True
recording = False

start_time = time.time()
counter = 0

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
