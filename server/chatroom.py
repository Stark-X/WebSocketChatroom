# -*- coding: utf-8 -*-

from tornado import websocket
from server import store
import json


class ChatRoomHandler(websocket.WebSocketHandler):
    name = ""

    def check_origin(self, origin):
        # disable check cross-site security
        return True

    def open(self):
        print("WebSocket Opened from %s" % (self.request.remote_ip,))

    def on_message(self, message):
        try:
            package = json.loads(message)
        except ValueError as e:
            print("Message: %s\nException: %s" % (message, e))
            self.write_message("Invalid json data")
        else:
            self.dispatch(package)

    def dispatch(self, package):
        if package["action"] == "add":
            store.add_to_connection_pool(self)
            self.name = package["name"]
            self.write_message("%s join to the chat room" % (self.name,))
        elif package["action"] == "say":
            self.broadcast("%s said: %s" % (self.name, package["message"]))
        elif package["action"] == "close":
            self.broadcast("%s leave the chat room" % (self.name,))
            self.close()

    @staticmethod
    def broadcast(message):
        for connection in store.get_connections():
            connection.write_message(message)

    def on_close(self):
        print("WebSocket Closed from %s" % (self.request.remote_ip,))
