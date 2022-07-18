import requests
import cv2

FORWARD_ON = '0'
FORWARD_OFF = '1'
BACKWARD_ON = '2'
BACKWARD_OFF = '3'
LEFT_ON = '4'
LEFT_OFF = '5'
RIGHT_ON = '6'
RIGHT_OFF = '7'

# your android phone local ip address
url = 'http://192.168.0.107:5000'


def probe_check(image):
    dimensions = image.shape
    middle_y = int(dimensions[0] / 2)
    # Get middle_row because camera is sideways when coming from phone
    middle_row = image[middle_y, :]
    length = len(middle_row)//2

    count_pixels = 0
    for pixel in range(length,355,-1):
        print(f"Pixel #: {pixel}")
        pixel_found = image[middle_y,pixel]
        image[middle_y,pixel] = 125
        print(f"Pixel found:{pixel_found}")
        if pixel_found == 0:
            count_pixels += 1
            print(f"count_pixels: {count_pixels}")
        if count_pixels >= 10:
            print("Black line ?!")
    cv2.imshow("Middle row", image)

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
