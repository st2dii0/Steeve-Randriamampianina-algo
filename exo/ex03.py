#!/usr/bin/python3

def anagrams(str1, str2):
    length1 = len(str1)
    length2 = len(str2)

    if length1 != length2:
        return False
    else:
        str1 = sorted(str1)
        str2 = sorted(str2)
        for i in range(0, length1):
            if str1[i] != str2[i]:
                return False
        return True
