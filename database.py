#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Database:
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
        return True
    def read(self, key):
        return self.list[key]
    def update(self, obj, key):
        self.list.update({key:obj})
        return True
    def delete(self, key):
        temp = self.list[key]
        del self.list[key]
        return temp

    def commit(self):
        # Serialization here:
        pass
    def find(self):
        # Find by object parametrs here:
        pass
    pass

# Debug:
if __name__ == '__main__':
    db = Database(name = 'tester')
    db.create('test')

    print(db.delete(0))
