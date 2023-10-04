#!/usr/bin/python3
for ascii_value in range(ord('z'), ord('a') - 1, -1):
    char = chr(ascii_value)
    if (ord('z') - ascii_value) % 2 == 1:
        char = char.upper()
    print("{}".format(char), end='')
