#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import websocket, web, ioloop


class ChatRoomHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        print(origin)
        return True

    def open(self):
        print("WebSocket Opened")

    def on_message(self, message):
        self.write_message("Somebody said: " + message)

    def on_close(self):
        print("WebSocket Closed")


if __name__ == '__main__':
    app = web.Application([
        (r"/", ChatRoomHandler),
    ])

    app.listen(8080)
    ioloop.IOLoop.current().start()
