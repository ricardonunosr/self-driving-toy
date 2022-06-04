import cv2
import time

capture = cv2.VideoCapture(1)

successful = True

start_time = time.time()
counter = 0

cv2.namedWindow("preview", cv2.WINDOW_NORMAL)
while successful:
    counter += 1

    successful, image = capture.read()

    cv2.imshow("preview", image)

finish_time = time.time()
fps = counter / (finish_time-start_time)
print('Frames per second: ' + str(fps))
capture.release()
cv2.destroyAllWindows()
