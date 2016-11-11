#!/usr/bin/env python3

# not actually recursive way, but the way I will did it. 
lst = [1, 3, 5, 7, 9]

def sum_list(inp):
    """Find the sum of all elem in the list"""
    result = 0
    for i in inp:
        result += i

    return result

print(sum_list(lst))

