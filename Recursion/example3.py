#!/usr/bin/env python3
# Converting int to str (recursive way)

def to_str(n, base):
    convertstring = '0123456789ABCDEF'
    if n < base:
        return convertstring[n]
    else:
        return to_str(n//base, base) + convertstring[n % base]

print(to_str(1453, 16))
