#!/usr/bin/env python3

# Anagram detection example, POC #1

keyword = 'python'
candidate = input("Our keyword is 'python' please enter your candidate word: ")


def check_anagram(word):
    result = 0 
    for i in list(str(word)):
        if i in keyword:
            result += 1
    if result == len(keyword):
        print("We've a winner here!")
    return result, keyword
    
print(check_anagram(candidate))
