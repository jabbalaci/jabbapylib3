#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Work with unicode texts.

# from jplib import ascii
"""

import re
import unicodedata


#def unicode_to_ascii(text):
#    try:
#        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
#    except TypeError:
#        pass
#
#    return text

def remove_accents(input_str):
    # http://stackoverflow.com/questions/517923
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nkfd_form if not unicodedata.combining(c)])


def remove_non_ascii(text):
    return ''.join(c for c in text if ord(c) < 128)


def encode(s):
    """
    Useful for printing unicode strings to the console.
    """
    return s.encode('utf-8')


def strip_control_characters(input):
    """
    From http://chase-seibert.github.com/blog/2011/05/20/stripping-control-characters-in-python.html .
    """
    if input:
        # unicode invalid characters
        RE_XML_ILLEGAL = '([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' +\
                         '|' +\
                         '([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' %\
                         (unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                          unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                          unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff))
        input = re.sub(RE_XML_ILLEGAL, "", input)

        # ascii control characters
        input = re.sub(r"[\x01-\x1F\x7F]", "", input)

    return input

#############################################################################

if __name__ == "__main__":
    text = "László"
    print(remove_accents(text))
    print(remove_non_ascii(text))
    print(strip_control_characters(text))
    print(encode(text))
