#!/usr/bin/env python3

# python way:

def python_way():
	print("Pleae enter your string")
	user_input = (list(input("> ")))
	user_input.reverse()
	user_input = (''.join(user_input))
	print("here is your reversed string: %s" % user_input)


def non_python_way():
	print("Please enter your string")
	user_input = input("> ")
	user_input_reversed = list()
	for i in user_input[::-1]:
		user_input_reversed.append(i)
	print("here is your reversed string: %s" % ''.join(user_input_reversed))

def main():
	# python_way()
	non_python_way()

main()