#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    else:
        argument_word = 'argument' if num_args == 1 else 'arguments'
        print(f"{num_args} {argument_word}:", end='')
        print()
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
