#!/usr/bin/env python
"""
Creates an HTTP server with basic auth and websocket communication.
"""
import os
import tornado.web
import tornado.ioloop
from routes import url_patterns
from camera import camera

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
