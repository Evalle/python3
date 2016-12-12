from bubble import bubblesort

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubblesort(lst)

def test_bubble():
    assert lst == [17, 20, 26, 31, 44, 54, 55, 77, 93] 
