#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
import pickle


class Client:
    def __init__(self, host='localhost', port='9999', *args, **kwargs):
        self.HOST = host
        self.PORT = port
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
            self.sock.connect((self.HOST, self.PORT)) # Open 
            self.sock.sendall(pickle.dumps(data)) # Serialize and send command with value.

            recieved = self.sock.recv(1024) # Recive server feedback.
            result = (pickle.loads(recieved)) # Deserialize received data.
        finally:
            self.sock.close()
            return(result)

# Debug:
if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999
    
    if len(sys.argv)==2:
        PORT = int(sys.argv[1].strip())
    if len(sys.argv)==3:
        HOST = str(sys.argv[1].strip())
        PORT = int(sys.argv[2].strip())

    c = Client(HOST, PORT)
    print (c.create('test'))
    print (c.create({1:'a'}))
    print (c.create('test2'))
    print (c.create('test3'))

    print (c.read(0))
    print (c.read(1))
    print (c.read(2))
    print (c.read(2))
    print (c.read(3))

    Obj={1:'a',2:'b'}
    print (c.update(Obj, 1))
    print (c.read(0))
    print (c.delete(1))
    print (c.read(1))
