#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
import pickle

Obj={1:'a',2:'b'}


HOST, PORT = 'localhost', 9999

class Client:
    def __init__(self):
        pass
        
    def create(self, value, key=0):
        command="create"
        data={'command':command, 'value':value, 'key':key}
        return self.send(data)
    def read(self, key):
        command="read"
        data={'command':command, 'key':key}
        return self.send(data)
    def update(self, value, key):
        command="update"
        data={'command':command, 'value':value, 'key':key}
        return self.send(data)
    def delete(self, key):
        command="delete"
        data={'command':command, 'key':key}
        return self.send(data)
    def send(self,data):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = False
        try:
            self.sock.connect((HOST, PORT))
            self.sock.sendall(pickle.dumps(data)) # Serialize and send command with value.

            recieved = self.sock.recv(1024)
            result = (pickle.loads(recieved))
        finally:
            self.sock.close()
            return(result)

# Debug:
if __name__ == '__main__':
    c = Client()
    print (c.create('test'))
    print (c.create({1:'a'}))
    print (c.create('test2'))
    print (c.create('test3'))


    #print (c.create(Obj,10))
    #print (c.read(10))
    #print (c.update(Obj, 10))
    #print (c.delete(100))
