#!/usr/bin/env python
"""
Creates an HTTP server with basic auth and websocket communication.
"""
import numpy as np 
import cv2
import base64
import os
# import webbrowser
import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback

camera = cv2.VideoCapture(0)

try:
    import cStringIO as io
except ImportError:
    import io

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        if message == "read_camera":
            self.camera_loop = PeriodicCallback(self.loop, 10)
            self.camera_loop.start()

    def loop(self):
        _, frame = camera.read()
        hello, image = cv2.imencode('.jpg', frame)
        self.write_message(base64.b64encode(image))


settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "template"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

application = tornado.web.Application(url_patterns, **settings)

if __name__ == "__main__":
    print 'Server Running...'
    print 'Press ctrl + c to close'
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    camera()
