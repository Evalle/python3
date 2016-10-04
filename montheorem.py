#!/usr/bin/env python3
import random, sys, string

quote = "methinks it is like a weasel"
quotelen = len(quote)

def generator(quotalen):
    """ generate random line """ 
    ranline = list()
    for i in range(quotelen):
        ranline.append(random.choice(string.ascii_lowercase+' '))
    return ''.join(ranline)

def score(quote,quotelen):
    """ compare random line with quote and mark it """ 
    ranline = generator(quotelen)
    scorenum = 0
    for i,k in zip(quote,ranline):
        if i == k:
            scorenum += 1
    print(quote)
    print(ranline)
    return scorenum

print(score(quote,quotelen))
