#!/usr/bin/env python3

import time

def find_minimum(n):
    ''' find minimum in the list, 
    n should be a list ''' 
    start = time.time()
    minimum = min(n)
    end = time.time()
    return minimum, end - start

for i in range(5):
    print("Minimum is %d required %10.7f seconds" % find_minimum(range(10000000))) 
