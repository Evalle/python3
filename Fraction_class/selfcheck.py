#!/usr/bin/env python3
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
        common = gcd(new_chis, new_znam)
        return Fraction(new_chis // common, new_znam // common)

    def get_chis(self):
        return self.chis

    def get_znam(self):
        return self.znam

    def __sub__(self, other_fr):
        new_chis = self.chis * other_fr.znam - other_fr.chis * self.znam
        new_znam = self.znam * other_fr.znam
        common = gcd(new_chis, new_znam)
        return Fraction(new_chis // common, new_znam // common)

    def __mul__(self, other_fr):
        new_chis = self.chis * other_fr.chis
        new_znam = self.znam * other_fr.znam
        common = gcd(new_chis, new_znam)
        return Fraction(new_chis // common, new_znam // common)

    def __truediv__(self, other_fr):
        new_chis = self.chis * other_fr.znam
        new_znam = self.znam * other_fr.chis
        common = gcd(new_chis, new_znam)
        return Fraction(new_chis // common, new_znam // common)

    def __eq__(self, other_fr):
        first_num = self.chis * other_fr.znam
        second_num = self.znam * other_fr.chis
        return first_num == second_num

    def __ne__(self, other_fr):
        first_num == self.chis * other_fr.znam
        second_num == self.chis * other_fr.znam
        return first_num != second_num
    
    def __lt__(self, other_fr):
        first_num = self.chis * other_fr.znam
        second_num = self.znam * other_fr.chis
        return first_num < second_num

    def __le__(self, other_fr):
        first_num = self.chis * other_fr.znam
        second_num = self.znam * other_fr.chis
        return first_num <= second_num

    def __gt__(self, other_fr):
        first_num = self.chis * other_fr.znam
        second_num = self.znam * other_fr.chis
        return first_num > second_num
 
    def __ge_(self, other_fr):
        first_num = self.chis * other_fr.znam
        second_num = self.znam * other_fr.chis
        return first_num >= second_num

f1 = Fraction(1,2)
f1.get_chis()
print(f1)
