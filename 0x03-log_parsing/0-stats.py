#!/usr/bin/python3
"""module to parse logs
"""
import re


def validate_format(url):
    """function to validate format

    Args:
        url (string): the string to be validated
    """
    pass


def sort_codes(codes):
    """function to sort status codes

    Args:
        codes (array of codes): array to be sorted
    """
    return sorted(codes.items())


def print_details(file_size, details):
    """function to print details

    Args:
        details (array of codes): array to be sorted
    """
    print(f'File size: {file_size}')
    for k, v in details.items():
        if v is not None and v != 0:
            print(f"{k}: {v}")


def parse_logs():
    """function to parse logs
    """
    pattern = re.compile(r'\b(\d+)\b$')

    log = input()
    
    counter = 0
    file_size = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    
    while log:
        if not validate_format(log):
            continue
        match = pattern.search(log)

        # Check if a match is found
        if match:
            file_size = match.group(1)
        counter += 1
        
    if counter % 10 == 0:
        print_details(file_size, codes)
    pass


if __name__ == '__main__':
    """to prevent execution when imported
    """
    parse_logs()
