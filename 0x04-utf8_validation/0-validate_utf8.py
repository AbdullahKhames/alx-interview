#!/usr/bin/python3
"""module to check validity of data set for utf-8"""


def validUTF8(data):
    """function to check validity of data set for utf-8

    Args:
        data (list of integers): set to be checked for utf-8 validity
    """
    # for c in data:
    #     if not validChar(c):
    #         return False
    # return True
    successive_10 = 0
    for b in data:
        b = bin(b).replace('0b','').rjust(8, '0')
        if successive_10 != 0:
            successive_10 -= 1
            if not b.startswith('10'):
                return False
        elif b[0] == '1':
                successive_10 = len(b.split('0')[0]) - 1
    return True


# def validChar(c):
#     """checks for single char

#     Args:
#         c (char): char to be checked for utf-8 validity
#     """
#     binary_string = getBinary(c)



# def getBinary(number):
#     """returns the binary representation of char

#     Args:
#         number (char): char to be converted
#     """
#     ans = ""
#     if ( number == 0 ):
#         return 0
#     while ( number ):
#         ans += str(number&1)
#         number = number >> 1        
#     ans = ans[::-1]
 
#     return ans 
