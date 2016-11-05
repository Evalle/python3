#!/usr/bin/env python3

class Node(object):

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = new_data

    def set_next(self, newnext):
        self.next = newnext
