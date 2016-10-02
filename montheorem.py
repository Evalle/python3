#!/usr/bin/env python3

import random
import sys

keystr = "methinks it is like a weasel"
resultstr = list()

def string_generator():
    """ generate random string and add it to resultstr (global) """
    global resultstr
    
    for l in range(27):
        resultstr.append(random.choice(" abcdefghijklmnopqrstuvwxyz"))
    resultstr =  ''.join(resultstr)
    return resultstr

def comparator():
    """ compare keystr with resultstr """ 
    global resultstr, keystr
    
    if resultstr == keystr:
        print("100%!")
        sys.exit(0)
#    else:
#        print("miss")

def iterator():
    """ run string_generator and compare it's result with keystring 1000 times """ 
    global resultstr, keystr
    
    i = 1000
    while i > 0:
        string_generator()
        comparator()

iterator()
