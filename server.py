#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import socket
import threading
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

class database:
    def __init__(self, name):
        self.name = name
        self.list = {}
    def create(self, obj, key=0):
        for x in self.list.keys():
            if key==x:
                key+=1
                continue
            else:
                break
        self.list[key]=obj
    def read(self, key):
        return self.list[key]
    def update(self, obj, key):
        self.list.update({key:obj})
    def delete(self, key):
        del self.list[key]

    def commit(self):
        # Serialization here:
        pass
    def find(self):
        # Find by object parametrs here:
        pass
    pass

# Debug:
if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
    pass 
