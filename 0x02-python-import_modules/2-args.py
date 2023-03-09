#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print("{} argument{}{}.".format(num_args, "" if num_args == 1 else "s", ":" if num_args else ""))
if num_args:
    for i, arg in enumerate(args):
        print("{}: {}".format(i+1, arg))
