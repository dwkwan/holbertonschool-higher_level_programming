#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if j > i and i < 8:
            print("{:d}".format(i), end="")
            print("{:d}, ".format(j), end="")
print("89")
