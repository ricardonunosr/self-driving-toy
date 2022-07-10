import requests
from pynput.keyboard import Key, Listener
import serial

# your android phone local ip address
url = 'http://192.168.0.101:5000'
last_key = str(Key.caps_lock)+"P"

FORWARD_ON = '0'
FORWARD_OFF = '1'
BACKWARD_ON = '2'
BACKWARD_OFF = '3'
LEFT_ON = '4'
LEFT_OFF = '5'
RIGHT_ON = '6'
RIGHT_OFF = '7'

#ser = serial.Serial('/dev/tty.usbmodem1101')
# print(ser.name)

# TODO: change left and right controls


def on_press(key):
    print('{0} pressed'.format(key))
    global last_key
    if str(key)+"P" != last_key:
        if key == Key.up:
            requests.post(url, FORWARD_ON)
            # ser.write(b'0')
        if key == Key.down:
            requests.post(url, BACKWARD_ON)
            # ser.write(b'2')
        if key == Key.right:
            requests.post(url, LEFT_ON)
            # ser.write(b'6')
        if key == Key.left:
            requests.post(url, RIGHT_ON)
            # ser.write(b'4')
    last_key = str(key)+"P"


def on_release(key):
    print('{0} released'.format(key))
    global last_key
    if str(key)+"R" != last_key:
        if key == Key.up:
            requests.post(url, FORWARD_OFF)
            # ser.write(b'1')

        if key == Key.down:
            requests.post(url, BACKWARD_OFF)
            # ser.write(b'3')
        if key == Key.right:
            requests.post(url, LEFT_OFF)
            # ser.write(b'7')
        if key == Key.left:
            requests.post(url, RIGHT_OFF)
            # ser.write(b'5')
    last_key = str(key)+"R"


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
