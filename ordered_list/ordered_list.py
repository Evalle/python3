#!/usr/bin/env python3

from node_example import Node

class OrderedList(object):

    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return size
