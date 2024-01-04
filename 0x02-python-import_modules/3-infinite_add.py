#!/usr/bin/python3
import sys

def add_arguments():
    return sum(int(arg) for arg in sys.argv[1:])

if __name__ == "__main__":
    print(add_arguments())
