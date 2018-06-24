from Controller.main import MainHandler
from Controller.socket import SocketHandler

url_patterns = [
    (r"/", MainHandler),
    (r'/ws', SocketHandler),
]
