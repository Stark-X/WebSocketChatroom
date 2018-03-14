#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import web, ioloop, options
from server.chatroom import ChatRoomHandler

if __name__ == '__main__':
    app = web.Application([
        (r"/", ChatRoomHandler),
    ])

    options.parse_config_file("./config/logger.conf")
    app.listen(8080)
    ioloop.IOLoop.current().start()
