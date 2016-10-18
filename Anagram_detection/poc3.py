#!/usr/bin/env python3

# Anagram detection example, POC #3
# O(n**2) or O(n logn) because of sorting operations


def anagram_solution(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches

print(anagram_solution('abcde', 'edcba'))
