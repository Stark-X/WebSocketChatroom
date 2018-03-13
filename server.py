#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import web, ioloop
from server.chatroom import ChatRoomHandler

if __name__ == '__main__':
    app = web.Application([
        (r"/", ChatRoomHandler),
    ])

    app.listen(8080)
    ioloop.IOLoop.current().start()
