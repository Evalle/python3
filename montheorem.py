#!/usr/bin/env python3
import random, sys, string

quote = "methinks it is like a weasel"

def generator():
    """ generate random line """ 
    ranline = list()
    for i in range(27):
        ranline.append(random.choice(string.ascii_lowercase+' '))
    return ''.join(ranline)

def score(quote):
    """ compare random line with quote and mark it """ 
    ranline = generator()
    scorenum = 0
    for i,k in zip(quote,ranline):
        print(i,k)
        if i == k:
            scorenum += 1
    score_percent = (scorenum * 27) / 100
    return score_percent

print(score(quote))
