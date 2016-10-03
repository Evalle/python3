#!/usr/bin/env python3

import random, sys, string

keystr = "methinks it is like a weasel"
resultstr = list()
quotelen = len(keystr)

def string_generator(resultstr):
    """ generate random string and add it to resultstr """
    for l in range(quotelen):
        resultstr.append(random.choice(string.ascii_lowercase+' '))
    resultstr =  ''.join(resultstr)
    return resultstr

def score(resultstr, keystr):
    """ compare keystr with resultstr and give the score for each compare """ 
    scorenum = 0
    keystr = keystr.split()
    resultstr = (''.join(resultstr)).split()
    for i,j in zip(keystr, resultstr):
        if i == j:
            scorenum += 1
    scorecount = (scorenum / quotelen) * 100
    print(resultstr)
    print(scorecount)

def iterator(resultstr, keystr):
    """ run string_generator and compare it's result with keystring 1000 times """ 
    i = 1000
    while i > 0:
        string_generator(resultstr)
        score(resultstr, keystr)
        i -= 1

iterator(resultstr, keystr)
