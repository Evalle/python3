#!/usr/bin/env python3

'''
Counts the number of individual words in a string. For added complexity read these 
strings in from a text file and generate a summary.
'''

import sys

'''
 in this example we have file as an input
 if you wabt to have direct user input 
 instead change 'direct_user_input' variable
 to True
 
'''
direct_user_input = False

if direct_user_input is False:
    try:
        file = open(sys.argv[1], 'r')
        
    except Exception as e:
        print(e)
        sys.exit(1)

    inp = file.read()

else: 
    inp = input('> ')

def counter_from_user_inp(inp, direct_user_input):
    
    if direct_user_input is True:
        print('----\n Attention!!!\n -----\n Words in direct input will be counted')    
    
    counter = 0
    
    for i in inp.split():
        if i not in ',.':
            counter += 1

    print(counter)

counter_from_user_inp(inp, direct_user_input)
