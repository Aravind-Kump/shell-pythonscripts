#!/usr/bin/python

val = float(input("Enter some integer:"))

if val >= 0:
    if val == 0:
        print("Value is zero")
    else:
        print("Value is +ve",val)
else:
    print("Val is negative",val)
