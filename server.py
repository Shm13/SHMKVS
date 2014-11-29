#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

class server:
    pass

# Debug:
if __name__ == '__main__':
    db = database('test')
    db.create('obj0')
    db.create('obj1')
    db.create('obj2')

    pass 
