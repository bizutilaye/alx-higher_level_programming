#!/usr/bin/python3
import sys

def print_stats():
    '''
        Printing statistics after every 10 lines and after keyboard interruption
    '''
    counter = 0
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for line in sys.stdin:
        line = line.split()
        try:
            total_size += int(line[-1])
            code = line[-2]
            status_codes[code] += 1
        except:
            continue
        if counter == 9:
            print("File size: {}".format(total_size))
            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            counter = 0
        counter += 1

    # printing statistics after keyboard interruption
    print("File size: {}".format(total_size))
    for key, val in sorted(status_codes.items()):
        if (val != 0):
            print("{}: {}".format(key, val))

if __name__ == "__main__":
    try:
        print_stats()
    except KeyboardInterrupt:
        print_stats()
