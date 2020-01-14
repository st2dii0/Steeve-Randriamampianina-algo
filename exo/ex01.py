#!/usr/bin/python3

def unique(str):
    for letter in str:
        counter = str.count(letter)
        while counts > 1:
            if counter != 0: 
                print(letter, counter)
                return False
            else:
                return True