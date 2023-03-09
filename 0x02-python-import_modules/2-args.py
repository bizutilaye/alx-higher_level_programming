#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    count = len(args)
    print(
        "{} argument{}{}".format(
            count, "" if count == 1 else "s", "." if count == 0 else ":"
        )
    )
    for i, arg in enumerate(args):
        print("{}: {}".format(i + 1, arg))
