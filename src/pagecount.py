import os.path
import socket

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import redis

from tornado.options import define, options
define("port", default=5000, help="run on the given port", type=int)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [(r"/", IndexHandler)]
                settings = dict(
				template_path=os.path.join(os.path.dirname(__file__), "tpl"),
				static_path=os.path.join(os.path.dirname(__file__), "static"),
				debug=True,
				)
		self.db = redis.Redis(host='redis',port=6379,db=0)
    	        self.db.set("visit:5000:totals",10)
		tornado.web.Application.__init__(self, handlers,**settings)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		count=self.application.db.incr("visit:5000:totals")
		hostname=socket.gethostname()
		self.render('index.html',pagecount=count,hostname=hostname)

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
