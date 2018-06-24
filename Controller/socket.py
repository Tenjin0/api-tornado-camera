from tornado import websocket
from tornado.ioloop import PeriodicCallback

import time
import base64
from io import BytesIO
import cv2
from PIL import Image

MAX_FPS = 10

cap = cv2.VideoCapture(0)


def camera():
    if cap.isOpened():
        hello, image = cap.read()
        hello, image = cv2.imencode('.jpg', image)
        buffer = BytesIO()
        img = Image.fromarray(image)
        img.save(buffer, format="png")
        return base64.b64encode(buffer.getvalue())


if __name__ == "__main__":
    while True:
        time.sleep(1./MAX_FPS)
        camera()
    pass


def base64_decode(data):
    format, imgstr = data.split(';base64,')
    return imgstr.decode('base64')


def base64_encode(data):
    if data:
        return 'data:image/png;base64,' + data


class SocketHandler(websocket.WebSocketHandler):
    """ Handler for websocket queries. """

    def __init__(self, *args, **kwargs):
        super(SocketHandler, self).__init__(*args, **kwargs)

    def open(self):
        pass

    def on_message(self, message):
        print(message)
