#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import web, ioloop, options
from server.chatroom import ChatRoomHandler

if __name__ == '__main__':
    app = web.Application([
        (r"/", ChatRoomHandler),
    ], websocket_ping_interval=3)

    options.parse_config_file("./config/logger.conf")
    app.listen(8080)
    ioloop.IOLoop.current().start()
