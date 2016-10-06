from selfcheck import * 

f1 = Fraction(1,2)
f2 = Fraction(2,3)

def test_chis():
    assert f1.get_chis() == 1
    assert f2.get_chis() == 2

def test_znam():
    assert f1.get_znam() == 2
    assert f2.get_znam() == 3

def test_frac():
    assert str(f1) == '1/2'
    assert str(f2) == '2/3'

def test_add():
    assert str(f1 + f2) == '7/6'

def test_sub():
    assert str(f1 - f2) == '-1/6'

def test_mul():
    assert str(f1 * f2) == '1/3'

def test_truediv():
    assert str(f1 / f2) == '3/4'

def test_ne():
    assert str(f1) != str(f2)

def test_lt():
    assert f1 < f2

def test_le():
    assert f1 <= f2

def test_gt():
    assert f2 > f1

def test_ge():
    assert f2 >= f1
