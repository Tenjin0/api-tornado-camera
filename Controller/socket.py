from tornado.ioloop import PeriodicCallback
import tornado.websocket
import cv2
import base64
camera = cv2.VideoCapture(0)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        if message == "read_camera":
            self.camera_loop = PeriodicCallback(self.loop, 10)
            self.camera_loop.start()

    def loop(self):
        _, frame = camera.read()
        hello, image = cv2.imencode('.jpg', frame)
        self.write_message(base64.b64encode(image))
