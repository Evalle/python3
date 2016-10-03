#!/usr/bin/env python3

import random, sys, string

keyStr = "methinks it is like a weasel"
resultstr = list()
quoteLen = len(keyStr)

def string_generator(resultstr):
    """ generate random string and add it to resultstr (global) """
    for l in range(27):
        resultstr.append(random.choice(string.ascii_lowercase+' '))
    resultstr =  ''.join(resultstr)
    return resultstr

def score(resultstr, keyStr):
    """ compare keystr with resultstr and give the score for each compare """ 
    resultstr = 
    for i,k in zip(


def iterator(resultstr, keyStr):
    """ run string_generator and compare it's result with keystring 1000 times """ 
    i = 1000
    while i > 0:
        string_generator(resultstr)
        comparator(resultstr, keystr)
        i -= 1
iterator(resultstr, keystr)
