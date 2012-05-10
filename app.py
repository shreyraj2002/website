# Python imports

# Tornado imports
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import options


import handlers
# Library imports


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(handlers.Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
