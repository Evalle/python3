#!/usr/bin/env python

import random

# lst is a list, e.g. input should be <1, 2, 3...>

def bbl_srt(n):

    changed = False

    while not changed:
        changed = True
        for i in range((len(n) - 1)):
            if n[i] > n[i + 1]:
                n[i], n[i + 1] = n[i + 1], n[i]
                changed = False
        return n

testset = [i for i in range(100)]
random.shuffle(testset)

print(testset)

print(bbl_srt(testset))

