#!/usr/bin/env python3

import sys

total_file_size = 0
status_codes_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for i, line in enumerate(sys.stdin):
        split_line = line.split()
        try:
            file_size = int(split_line[-1])
            status_code = split_line[-2]
        except (IndexError, ValueError):
            continue

        total_file_size += file_size
        status_codes_count[status_code] += 1

        if (i + 1) % 10 == 0:
            print("File size: {}".format(total_file_size))
            for status_code, count in sorted(status_codes_count.items()):
                if count != 0:
                    print("{}: {}".format(status_code, count))
            print()

except KeyboardInterrupt:
    print("File size: {}".format(total_file_size))
    for status_code, count in sorted(status_codes_count.items()):
        if count != 0:
            print("{}: {}".format(status_code, count)))
