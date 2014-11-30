#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import socketserver
import pickle
import sys
from database import Database

db = Database('testing')

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("Sender: %s"%(self.client_address[0]))
        print("Received %d byte: %s"%(len(self.data),self.data))

        result = self.parser(self.data)

        self.request.sendall(result)

    def parser(self, raw_data):
        data = pickle.loads(raw_data)
        if data['command']=='create':
            return db.create(data['value'],data['key'])
        elif data['command']=='read':
            return db.read(data['key'])
        elif data['command']=='update':
            return db.update(data['value'],data['key'])
        elif data['command']=='delete':
            return db.delete(data['key'])
        else:
            # Unknown command.
            pass

# Debug:
if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999
    
    if len(sys.argv)==2:
        PORT = int(sys.argv[1].strip())
        
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
