from Controller.main import MainHandler
from Controller.socket import WebSocketHandler

url_patterns = [
    (r"/", MainHandler),
    (r'/ws', WebSocketHandler)
]
