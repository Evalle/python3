string = list('((()))')

def balance(inp):
    balanced = True
    a = list()
    for i in inp:
        if i == '(':
            a.append(i)
        else:
            if len(a) == 0:
                balanced = False 
            else:
                a.pop()
    return balanced

print(balance(string))
