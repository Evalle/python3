#!/usr/bin/env python3

# Basic implementation of stack in python3


class Stack(object):

    def __init__(self):
        self.items = list()

    def show(self):
        return self.items

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def reverse(self):
        return self.items.reverse()
