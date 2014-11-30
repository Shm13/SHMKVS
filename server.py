#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import socketserver
import pickle
from database import Database

db = Database('testing')

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        print(pickle.loads(self.data))
        self.request.sendall(self.data)

    def parser(self, raw_data):
        data = pickle.loads(raw_data)
        if data['command']=='create':
            db.create(data.obj,data.id)
        elif data['command']=='read':
            temp = db.read(data.id)
            return{'obj':temp,'key':data.key}
        elif data['command']=='update':
            db.update(data.obj,data.id)
        elif data['command']=='delete':
            temp = db.delete(data.id)
            return{'obj':temp,'key':data.key}
        else:
            # Unknown command.
            pass
        

# Debug:
if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
