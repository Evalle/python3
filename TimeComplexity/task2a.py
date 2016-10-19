#!/usr/bin/env python3

# this snippet proves that get item operation is O(1) for dictionaries 

import timeit, random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x.get(random.randrange(%d))" % i, 
            "from __main__ import random, x")
    
    x = {j:None for j in range(i)}
    d_time = t.timeit(number = 1000)
    print("%d, %10.3f" % (i, d_time))
