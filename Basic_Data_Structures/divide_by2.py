inp = int(input('> '))

def divide_by2(inp):
    a = list()
    while inp > 0:
        rem = inp % 2
        a.append(rem)
        inp = inp // 2
    a.reverse()
    return ''.join(str(i) for i in a)

print(divide_by2(inp))
