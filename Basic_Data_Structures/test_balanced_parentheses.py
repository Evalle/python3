from balanced_parentheses import balance

def balance_test1():
    assert balance('((()))') == True
    
def balance_test2():    
    assert balance(')))') == False
