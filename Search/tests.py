#!/usr/bin/env python3 

from sequential import sequential_search

lst = [1,2,3,4,5,6]

def test_item_in_list():
    assert sequential_search(lst, 3) is True

def test_item_not_in_the_list():
    assert sequential_search(lst, 7) is False
