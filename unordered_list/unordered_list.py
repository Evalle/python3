#!/usr/bin/env python3

from node_example import Node

class UnorderedList(object):
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0 
        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if item == current.get_data():
                found = True
            else:
                current = current.get_next()

        return found

