import requests
from pynput.keyboard import Key, Listener

# your android phone local ip address
url = 'http://192.168.1.65:5000'
last_key = str(Key.caps_lock)+"P"


def on_press(key):
    print('{0} pressed'.format(key))
    global last_key
    if str(key)+"P" != last_key:
        if key == Key.up:
            requests.post(url, data='1')
        if key == Key.down:
            requests.post(url, data='2')
        if key == Key.right:
            requests.post(url, data='6')
        if key == Key.left:
            requests.post(url, data='4')
    last_key = str(key)+"P"


def on_release(key):
    print('{0} released'.format(key))
    global last_key
    if str(key)+"R" != last_key:
        if key == Key.up:
            requests.post(url, data='0')
        if key == Key.down:
            requests.post(url, data='3')
        if key == Key.right:
            requests.post(url, data='7')
        if key == Key.left:
            requests.post(url, data='5')
    last_key = str(key)+"R"


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
