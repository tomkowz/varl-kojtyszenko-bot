import tornado.ioloop
import tornado.web

from info_handler import InfoHandler
from perform_next_move_handler import PerformNextMoveHandler
from ping_handler import PingHandler

application = tornado.web.Application([
    (r"/", PingHandler),
    (r"/info", InfoHandler),
    (r"/PerformNextMove", PerformNextMoveHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
