#!/usr/bin/env python3
# Write a function that takes a string as a parameter and returns a new
# string that is the reverse of the old string.

def str_rev_recur(inp):
    inp = str(inp)
    if len(inp) == 1:
        return inp
    else:
        return str_rev_recur(inp[1:]) + inp[0]

def str_reverse_non_recur(inp):
    inp = list(inp)
    new_str = list()
    if len(inp) == 1:
        return inp
    else:
        for i in range(len(inp)):
            new_str.append(inp.pop())
        return ''.join(new_str)

print(str_reverse_non_recur('random'))
print(str_rev_recur('random'))
