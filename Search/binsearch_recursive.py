#!/usr/bin/env python3

# Simple implementation of the recursive binary search
# complexety = n/2**i == O(log n)

def binary_search(lst, item):

    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == item:
            return True
        else:
            if item < lst[midpoint]:
                return binary_search(lst[:midpoint], item)
            else:
                return binary_search(lst[midpoint + 1:], item)
