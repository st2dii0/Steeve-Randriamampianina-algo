#!/usr/bin/python3

def reverse(str):
    # return str[::-1] # easy answer
    
    # other one
    rev = ''
    i = len(str)
    while i > 0:
        rev += str[ i - 1]
        i -= 1
    return rev