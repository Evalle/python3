#!/usr/bin/env python3
# palyndrome checker

from deque import Deque

def palchecker(string):
    new_deque = Deque()
    for i in string:
        new_deque.add_rear(i)

    still_equal = True

    while new_deque.size() > 1 and still_equal:
        first = new_deque.remove_rear()
        last = new_deque.remove_front()
        if first != last:
            still_equal = False

    return still_equal

print(palchecker('radar'))
print(palchecker('asdsdad'))
