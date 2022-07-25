import requests
import cv2

FORWARD_ON = "0"
FORWARD_OFF = "1"
BACKWARD_ON = "2"
BACKWARD_OFF = "3"
LEFT_ON = "4"
LEFT_OFF = "5"
RIGHT_ON = "6"
RIGHT_OFF = "7"

# your android phone local ip address
url = "http://192.168.0.107:5000"

MIN_BLACK_PIXELS = 15


def probe_check_forward(image):
    dimensions = image.shape
    middle_y = int(dimensions[0] / 2)
    # Get middle_row because camera is sideways when coming from phone
    middle_row = image[middle_y, :]
    length = len(middle_row) // 2

    count_pixels = 0
    for pixel in range(length, length - 400, -1):
        pixel_found = image[middle_y, pixel]
        image[middle_y, pixel] = 125
        if pixel_found == 0:
            count_pixels += 1
        else:
            # Reset if not in a row
            count_pixels = 0
        if count_pixels >= MIN_BLACK_PIXELS:
            print("Black line ?!")
            return False
    return True


def probe_check_right(image):
    dimensions = image.shape
    middle_x = int(dimensions[1] / 2)
    middle_col = image[:, middle_x]
    length = len(middle_col) // 2

    count_pixels = 0
    for pixel in range(length, 355, -1):
        pixel_found = image[pixel, middle_x]
        image[pixel, middle_x] = 125
        if pixel_found == 0:
            count_pixels += 1
        else:
            # Reset if not in a row
            count_pixels = 0
        if count_pixels >= MIN_BLACK_PIXELS:
            print("Black line ?!")
            return False
    return True


def move_forward():
    requests.post(url, FORWARD_ON)


def stop_forward():
    requests.post(url, FORWARD_OFF)


def move_backward():
    requests.post(url, BACKWARD_ON)


def stop_backward():
    requests.post(url, BACKWARD_OFF)


def move_left():
    requests.post(url, LEFT_ON)


def stop_left():
    requests.post(url, LEFT_OFF)


def move_right():
    requests.post(url, RIGHT_ON)


def stop_right():
    requests.post(url, RIGHT_OFF)


def stop_car():
    requests.post(url, FORWARD_OFF)
    requests.post(url, BACKWARD_OFF)
    requests.post(url, LEFT_OFF)
    requests.post(url, RIGHT_OFF)
