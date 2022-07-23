from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from usb4a import usb
from usbserial4a import serial4a
from pprint import pprint
import http.server
from jnius import autoclass
from android.runnable import run_on_ui_thread

WindowManager = autoclass('android.view.WindowManager$LayoutParams')
activity = autoclass('org.kivy.android.PythonActivity').mActivity


usb_device_list = usb.get_usb_device_list()
usb_device_name_list = [device.getDeviceName() for device in usb_device_list]
usb_device_dict = {
    device.getDeviceName(): [            # Device name
        device.getVendorId(),           # Vendor ID
        device.getManufacturerName(),   # Manufacturer name
        device.getProductId(),          # Product ID
        device.getProductName()         # Product name
    ] for device in usb_device_list
}
pprint(usb_device_dict)

if usb_device_list:
    serial_port = serial4a.get_serial_port(
        usb_device_list[0].getDeviceName(),
        9600,   # Baudrate
        8,      # Number of data bits(5, 6, 7 or 8)
        'N',    # Parity('N', 'E', 'O', 'M' or 'S')
        1)      # Number of stop bits(1, 1.5 or 2)


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print("Body: ", body)
        self.send_response(200)
        self.end_headers()
        serial_port.write(body)
        # print(serial_port.read())


class HttpServerKivy(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(HttpServerKivy, self).__init__(*args, **kwargs)
        self.start_server()
        self.full_screen()

    @run_on_ui_thread
    def full_screen(self):
        window = activity.getWindow()
        window.addFlags(WindowManager.FLAG_FULLSCREEN)

    def start_server(self, HandlerClass=SimpleHTTPRequestHandler, ServerClass=http.server.HTTPServer):
        server_address = ('192.168.0.107', 5000)
        httpd = ServerClass(server_address, HandlerClass)
        httpd.serve_forever()


class App(App):
    def build(self):
        return HttpServerKivy()


if __name__ == '__main__':
    App().run()
