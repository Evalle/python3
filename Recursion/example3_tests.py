from example3 import to_str

def test_n_int():
    assert to_str(3, 10) == '3'

def test_n_dec():
    assert to_str(1453, 16) == '5AD'

def test_b_bin():
    assert to_str(10, 2) == '1010'
