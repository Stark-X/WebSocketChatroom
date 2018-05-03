# -*- coding: utf-8 -*-

from tornado import websocket
from server import operator
import logging
import json


class ChatRoomHandler(websocket.WebSocketHandler):
    name = ""
    
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self._general_logger = logging.getLogger()

    def check_origin(self, origin):
        # disable check cross-site security
        return True

    def open(self):
        self._general_logger.info("WebSocket Opened from %s" % (self.request.remote_ip,))

    def on_message(self, message):
        try:
            package = json.loads(message)
            operator.validation(package)
        except ValueError as e:
            self._general_logger.error("Message: %s\nException: %s" % (message, e))
            self.write_message("Invalid json data")
        except Exception as e:
            self._general_logger.error("Message: %s\nException: %s" % (message, e))
            self.write_message("Invalid package data")
        else:
            operator.dispatch(self, package)

    def on_close(self):
        self._general_logger.info("WebSocket Closed from %s" % (self.request.remote_ip,))
