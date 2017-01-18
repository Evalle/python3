#!/usr/bin/env python3

''' 
Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it 
reads the same forwards as backwards like “racecar”
'''

user_input = (input('> ').lower())


def reverse_function(inp):
    user_input_list = list(user_input)
    reverse = ''.join((user_input_list[::-1]))
    return reverse


def main(inp):
    if user_input == reverse_function(inp):
        print('Palindrome!')
    else:
        print('Not Palindrome!')


main(user_input)
