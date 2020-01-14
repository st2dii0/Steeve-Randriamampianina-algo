#!/usr/bin/python3

def removeDuplicate(str):
    list = []
    for i in str:
        if i not in list:
            list.append(i)
    return list