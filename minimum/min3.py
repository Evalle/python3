#!/usr/bin/env python3

import time
from random import randrange

def find_minimum(alist):
    ''' calsulates the minimum in the list
    O(n**2) (NON-OPTIMAL!) way ''' 
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin

for i in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(i)]
    start = time.time()
    print(find_minimum(alist))
    end = time.time()
    print("Size: %d time %f" % (i, end - start))
