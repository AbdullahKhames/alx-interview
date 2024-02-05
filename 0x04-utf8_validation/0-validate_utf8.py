#!/usr/bin/python3
"""module to check validity of data set for utf-8"""


def validUTF8(data):
    """function to check validity of data set for utf-8

    Args:
        data (list of integers): set to be checked for utf-8 validity
    """
    for i in range(len(data)):
            if data[i] < 0 or data[i] > 255:
                # handle only the 8 least significant bits
                data[i] = int(bin(data[i])[-8:], 2)
    try:
        bytes(data).decode(encoding='utf-8', errors='strict')
        return True
    except Exception:
        return False
