#!/usr/bin/env python3

from stack import Stack

def parchecker(inpstring):
    s = Stack()
    balanced = True
    index = 0
    while index < len(inpstring) and balanced:
        symbol = inpstring[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isempty():
                balanced = False
            else:
                s.pop()

        index += 1
        
    if balanced and s.isempty():
        return True
    else:
        return False

print(parchecker('((()))'))
print(parchecker('(()'))
