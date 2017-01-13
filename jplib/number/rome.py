#!/usr/bin/env python3

"""
Convert Roman numbers to decimal.
Convert decimal to Roman numbers.

It's just a wrapper for the module
romanclass (http://pypi.python.org/pypi/romanclass).

# from jplib.number import rome as roman
"""

if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from jplib.lib import romanclass as roman


def roman_to_decimal(num):
    """
    Convert a Roman number to decimal.

    >>> roman_to_decimal('MCMLXXVII')
    1977
    """
    return roman.fromRoman(num)


def decimal_to_roman(num):
    """
    Convert a decimal number to Roman.

    >>> decimal_to_roman(49)
    'XLIX'
    """
    return roman.toRoman(num)


def simplify_roman(num):
    """
    Given a Roman number, simplify it.

    >>> simplify_roman('IIII')
    'IV'
    """
    return decimal_to_roman(roman_to_decimal(num))

#############################################################################

if __name__ == "__main__":
    print(roman_to_decimal('MCMLXXVII'))
    print(roman_to_decimal('MMMMMMDCLXXII'))
    #
    print(decimal_to_roman(49))
    print(simplify_roman('IIII'))
