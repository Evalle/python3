#!/usr/bin/env python3
import random, sys, string

quote = "methinks it is like a weasel"

def generator(quote):
    """ generate random line """ 
    ranline = list()
    for i in range(len(quote)):
        ranline.append(random.choice(string.ascii_lowercase+' '))
    return ''.join(ranline)

def score(quote):
    """ compare random line with quote and mark it """ 
    ranline = generator(quote)
    scorenum = 0
    for i,k in zip(quote,ranline):
        print(i,k)
        if i == k:
            scorenum += 1
    score_percent = (scorenum / len(quote)) * 100
    print(scorenum)
    return score_percent

print(score(quote))
