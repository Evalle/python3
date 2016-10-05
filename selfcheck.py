#!/usr/bin/env python
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:

    def __init__(self, top, bottom):
        self.chis = top
        self.znam = bottom

    def __str__(self):
        return str(self.chis) + '/' + str(self.znam)

    def __add__(self, other_fr):
        new_chis = self.chis * other_fr.znam + other_fr.chis * self.znam
        new_znam = self.znam * other_fr.znam
        return Fraction(new_chis, new_znam)


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)
