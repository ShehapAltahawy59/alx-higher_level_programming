#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("Number of arguments: 0.")
    elif arg_count == 1:
        print(f"Number of argument: 1:")
    else:
        print(f"Number of arguments: {arg_count}:")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
