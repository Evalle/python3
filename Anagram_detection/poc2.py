#!/usr/bin/env python3

# Anagram detection example, POC #2
# o(n**2)


def anagram_search(s1, s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK

print(anagram_search('abcd', 'dcba'))
