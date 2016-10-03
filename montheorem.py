#!/usr/bin/env python3

import random, sys, string

keystr = "methinks it is like a weasel"
resultstr = list()
quotelen = len(keystr)

def string_generator():
    """ generate random string and add it to resultstr """
    chars = string.ascii_lowercase+' '
    for l in range(quotelen):
        resultstr.append(random.choice(chars))
    resultstr =  ''.join(resultstr)
    return resultstr

def score():
    """ compare keystr with resultstr and give the score for each compare """ 
    scorenum = 0
    keystr = keystr.split()
    resultstr = (''.join(resultstr)).split()
    for i,j in zip(keystr, resultstr):
        if i == j:
            scorenum += 1
    scorecount = (scorenum / quotelen) * 100
    print(keystr)
    print(resultstr)
    print(scorecount)

def iterator():
    """ run string_generator and compare it's result with keystring 1000 times """ 
    i = 3
    while i > 0:
        string_generator()
        score()
        i -= 1

iterator()
