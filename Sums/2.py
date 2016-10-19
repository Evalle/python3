#!/usr/bin/env python3
import time

def sum_of_n(n):
    start = time.time()
    sumn = (n*(n+1))/2
    end = time.time()
    return sumn, end - start

for i in range(5): 
    print("Sum is %d required %10.7f seconds" % sum_of_n(1000))
