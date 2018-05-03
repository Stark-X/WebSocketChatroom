# -*- coding:utf-8 -*-

from . import store

def validation(package):
    if type(package)!=dict or "action" not in package:
        raise Exception("Invalid data")

def dispatch(connection, package):
    if package["action"] == "add":
        join_room(connection, package)
    elif package["action"] == "say":
        say_to_all(connection, package)
    elif package["action"] == "close":
        leave_room(connection, package)

def broadcast(message):
    for connection in store.get_connections():
        connection.write_message(message)

def join_room(connection, package):
    store.add_to_connection_pool(connection)
    connection.name = package["name"]
    connection.write_message("%s join to the chat room" % (connection.name,))

def say_to_all(connection, package):
    if connection.name == "":
        connection.write_message("Please register.")
    else:
        broadcast("%s said: %s" % (connection.name, package["message"]))

def leave_room(connection, package):
    broadcast("%s leave the chat room" % (connection.name,))
    store.rm_from_connection_pool(connection)
    connection.close()
