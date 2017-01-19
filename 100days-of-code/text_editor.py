#!/usr/bin/env python3

'''
Text Editor - Notepad style application that can open, edit, and save text documents. 
Optional: Add syntax highlighting and other features.
'''

print("Text Editor\n 'e' - for edit\n 'o' - for open \n")

file_name = ('example.txt')

user_input = (input('> ').lower())

if 'o' or 'open' in user_input:
    print('name of the file?')
    file_name = input()
    print(file_name)
    open(file_name, 'w')

