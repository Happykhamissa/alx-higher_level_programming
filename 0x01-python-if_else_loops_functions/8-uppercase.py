#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        char = ord(str[c])
        if 97 <= ord(char) <= 122:
            char = char - 32
        print("{:c}".format(char), end="")
    print()
