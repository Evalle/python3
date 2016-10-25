inp = int(input('number: '))
base = int(input('base: '))

def divide_by(inp, base):
    digits = '0123456789ABCDEF'
    a = list()
    while inp > 0:
        rem = inp % base
        rem = digits[rem]
        a.append(rem)
        inp = inp // base
    a.reverse()
    return ''.join(str(i) for i in a)

print(divide_by(inp, base))
