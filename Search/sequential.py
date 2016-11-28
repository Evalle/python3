#!/usr/bin/env python3
# sequential search
# list is not ordered in any way

def sequential_search(lst, item):

    pos = 0
    found = False

    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
        else:
            pos += 1

    return found
