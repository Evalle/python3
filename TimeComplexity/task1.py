#!/usr/bin/env python3

# This snippet proves that the list index operator is O(1)

import timeit, random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x[random.randrange(%d)]" % i, 
            "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number = 1000)
    print("%d, %10.3f" % (i, lst_time))
