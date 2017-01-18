#!/usr/bin/env python3

'''
Count Vowels - Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.
'''

user_input = input("> ")
vowels = "aeiou"


def counter(inp, seq):
	count = 0
	for i in inp:
		if i in seq:
			count += 1
	print(count)


def result(inp, seq):
	rslt = dict()
	for i in inp.lower():
		if i in seq:
			if i not in rslt:
				rslt[i] = 1
			else:
				rslt[i] += 1  

	for k,v in rslt.items():	
		print("%s - %s" % (k,v))


def main(inp, seq):
	counter(inp, seq)
	result(inp, seq)

main(user_input, vowels)