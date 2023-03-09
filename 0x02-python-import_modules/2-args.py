#!/usr/bin/python3
if __name__ == "__main__":
    import sys

args = sys.argv[1:]
num_args = len(args)

print(f"Number of argument(s): {num_args} {'argument' if num_args == 1 else 'arguments'}{'.' if num_args == 0 else ':'}\n")

for i, arg in enumerate(args, 1):
    print(f"Argument {i}: {arg}")

