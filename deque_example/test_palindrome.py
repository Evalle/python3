from palindrome import palchecker

def test_palchecker1():
    assert palchecker('radar') == True

def test_palchecker2():
    assert palchecker('asdsad') == False
