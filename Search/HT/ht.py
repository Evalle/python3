#!/usr/bin/env python3

# HashTable Class

class HashTable(class):

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
