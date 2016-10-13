#!/usr/bin/env python3
import random, sys, string

quote = "methinks it is like a weasel"

def generator(quote):
    """ generate random line """ 
    ranline = list()
    for i in range(len(quote)):
        ranline.append(random.choice(string.ascii_lowercase+' '))
    return ''.join(ranline)

def score(quote, ranstr):
    """ compare random line with quote and mark it """ 
    scorenum = 0
    for i, k in zip(quote, ranstr):
        if i == k:
            scorenum += 1
    score_percent = (scorenum / len(quote)) * 100
    rounded_percent = round(score_percent)
    return rounded_percent

def runner(quote):
    """ run score function 10 million times 
    and find out the biggest hit """ 
    ranline = generator(quote)
    biggest = 0
    i = 100000000
    while i > 0:
        result = (score(quote, ranline))
        if result > biggest:
            biggest = result
            print(ranline)
            if biggest == 100:
                sys.exit(0)
        i -= 1
    print("====")
    print(biggest)

runner(quote)
