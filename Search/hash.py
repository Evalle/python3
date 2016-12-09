#!/usr/bin/env python3 

# simple implementation of hash function

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum % tablesize
