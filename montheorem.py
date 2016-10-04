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

print(generator(quotelen))
