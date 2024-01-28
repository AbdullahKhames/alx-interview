#!/usr/bin/python3
"""module to parse logs
"""
import re
import sys


sizes = [0]
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def validate_format(log):
    """function to validate format

    Args:
        log (string): the string to be validated
    """
    pattern = (r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
               r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
               r'"GET /projects/260 HTTP/1.1" \d{3} \d+$')
    return bool(re.match(pattern, log))


def parse_logs():
    print('File size: {}'.format(sum(sizes)))
    for s_code, count in sorted(codes.items()):
        if count:
            print('{}: {}'.format(s_code, count))


try:
    for i, line in enumerate(sys.stdin, start=1):
        matches = line.rstrip().split()
        try:
            status_code = matches[-2]
            file_size = matches[-1]
            if status_code in codes.keys():
                codes[status_code] += 1
            sizes.append(int(file_size))
        except Exception:
            pass
        if i % 10 == 0:
            parse_logs()
    parse_logs()
except KeyboardInterrupt:
    parse_logs()
    raise


if __name__ == '__main__':
    """to prevent execution when imported
    """
    parse_logs()
