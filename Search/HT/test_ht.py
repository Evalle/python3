# tests for HashTable class

from ht import HashTable

H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

def test_slots():
    assert H.slots == [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]

def test_data():
    assert H.data == ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion',
                   'tiger', None, None, 'cow', 'cat']


