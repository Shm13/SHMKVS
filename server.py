#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import socketserver
from database import Database

db = Database('testing')

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data)


# Debug:
if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
