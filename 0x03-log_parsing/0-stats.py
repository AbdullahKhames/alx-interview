#!/usr/bin/python3
"""module to parse logs
"""
import re


def validate_format(log):
    """function to validate format

    Args:
        log (string): the string to be validated
    """
    pattern = (r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 '
               r'HTTP/1.1" \d{3} \d+$')
    return bool(re.match(pattern, log))


def print_details(file_size, details):
    """function to print details

    Args:
        file_size: the size of the files
        details (array of codes): array to be sorted
    """
    print(f'File size: {file_size}')
    for k, v in details.items():
        if v is not None and v != 0:
            print(f"{k}: {v}")


def parse_logs():
    """function to parse logs
    """
    pattern = r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)'

    log = input()

    counter = 0
    file_size = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    while log != '':
        try:
            if not validate_format(log):
                log = input()
                continue
            # Use re.search to find the match in the line
            match = re.search(pattern, log)
            # Check if a match is found
            if match:
                status_code = int(match.group(1))
                if status_code in codes:
                    codes[status_code] += 1
                file_size += int(match.group(2))
            counter += 1

            if counter % 10 == 0:
                print_details(file_size, codes)
            log = input()
        except KeyboardInterrupt as ex:
            print_details(file_size, codes)
            continue


if __name__ == '__main__':
    """to prevent execution when imported
    """
    parse_logs()
