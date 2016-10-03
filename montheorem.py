#!/usr/bin/env python3

import random
import sys

keystr = "methinks it is like a weasel"
resultstr = list()

def string_generator(resultstr):
    """ generate random string and add it to resultstr (global) """
    for l in range(27):
        resultstr.append(random.choice(" abcdefghijklmnopqrstuvwxyz"))
    resultstr =  ''.join(resultstr)
    return resultstr

def comparator(resultstr, keystr):
    """ compare keystr with resultstr """ 
    resultstr = ''.join(resultstr)
    if resultstr == keystr:
        print("100%!")
        sys.exit(0)
    else:
        print(resultstr)

def iterator(resultstr, keystr):
    """ run string_generator and compare it's result with keystring 1000 times """ 
    i = 1000
    while i > 0:
        string_generator(resultstr)
        comparator(resultstr, keystr)

iterator(resultstr, keystr)
