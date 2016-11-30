#!/usr/bin/env python3

# simple implementation of the binary search


def binary_search(lst, item):

    first = 0
    found = False
    last = len(lst) - 1

    while first <= last and not found:
        midpoint = (fitst + last) / 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                firt = midpoint + 1

        return found
