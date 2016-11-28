#!/usr/bin/env python3 

from seqorsearch import ordseqsearch

lst = [0,1,2,3,4,5,6,7,19,32]

def test_item_in_list():
    assert ordseqsearch(lst, 3) is True

def test_item_not_in_the_list():
    assert ordseqsearch(lst, 31) is False
