#!/usr/bin/python3

"""
    - Reads stdin line by line and computes metrics
    - Input format:
 <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
        (if the format is not this one, the line must be skipped)

    - After every 10 lines and/or a keyboard interruption (CTRL + C),
      print these statistics from the beginning:
    - Total file size: File size: <total size>
        - where <total size> is the sum of all previous <file size>
        - Number of lines by status code:
            - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            - if a status code doesn’t appear or is not an integer,
              don’t print anything for this status code
            - format: <status code>: <number>
            - status codes should be printed in ascending order
"""


import sys


def print_info():
    """
        Prints total file size with each status code in
        ascending order
    """
    print('File size: {}'.format(total))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
count = total = 0

try:
    for line in sys.stdin:
        tokens = line.split(" ")
        if len(tokens) > 4:
            code = tokens[-2]
            size = int(tokens[-1])
            if code in status_codes.keys():
                status_codes[code] += 1
            total += size
            count += 1
        if count == 10:
            print_info()
            count = 0

except Exception:
    pass

finally:
    print_info()
