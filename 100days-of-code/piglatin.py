#!/usr/bin/env python3 

'''
Pig Latin is a game of alterations played on the English language 
game. To create the Pig Latin form of an English word the initial 
consonant sound is transposed to the end of the word and an 'ay' is 
affixed (Ex.: "banana" would yield 'ananabay')
'''

print("Please, enter your word")
user_input = (input('> ')).lower()

if user_input.isalpha() and len(user_input) > 0:
	end = 'ay'
	begin = user_input[0]
	if begin in 'aeiou':
		print(user_input + end)
	else:
		print(user_input[1:-1] + begin + end)
else:
	print('You should enter the word')