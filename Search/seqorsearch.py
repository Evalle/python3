#!/usr/bin/env python3
# Sequential search in ordered list


def ordseqsearch(lst, item):

    pos = 0
    found = False
    stop = False

    while pos < len(lst) and not found and not stop:
        if lst[pos] == item:
            found = True
        else:
            if lst[pos] > item:
                stop = True
            else:
                pos += 1

    return found
