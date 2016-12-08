from binsearch_recursive import binary_search

testlst = [0, 1, 2, 8, 13, 17, 19, 32, 42]


def test_binsearch_false():
    assert binary_search(testlst, 3) is False


def test_binsearch_true():
    assert binary_search(testlst, 13) is True
