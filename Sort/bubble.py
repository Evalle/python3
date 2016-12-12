#!/usr/bin/env python3

# Simple example of bubble sort in Python 3


def bubble(lst):

    for passnum in range(len(lst) - 1, 0, 1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
