#!/usr/bin/env python3

print("Pleae enter your string")
user_input = (list(input("> ")))
user_input.reverse()
user_input = (''.join(user_input))
print("here is your reversed string: %s" % user_input)