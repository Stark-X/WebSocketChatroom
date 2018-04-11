# -*- coding:utf-8 -*-

connections = set()


def add_to_connection_pool(connection):
    connections.add(connection)


def get_connections():
    return connections

def rm_from_connection_pool(connection):
    connections.remove(connection)
