#!/usr/bin/env python3

import time

def find_minimum(n):
    ''' calculates the minimum in the list
    n should be a list ''' 
    start = time.time()
    minim = n[0]
    for i in n:
        if i < minim:
            i = minim
    end = time.time()
    return minim, end - start 

for i in range(5):
    print("Minimum is %d required %10.7f seconds" % find_minimum(range(10000000)))
