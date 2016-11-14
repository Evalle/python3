from example4 import str_rev_recur, str_rev_non_recur

def test_rev_recur():
    assert str_rev_recur('random') == 'modnar'

def test_rev_non_recur():
    assert str_rev_non_recur('random') == 'modnar'
