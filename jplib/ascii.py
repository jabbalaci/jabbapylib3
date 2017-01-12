#!/usr/bin/env python3

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

def remove_accents(text):
    """
    >>> remove_accents('árvíztűrő tükörfúrógép')
    'arvizturo tukorfurogep'
    >>> remove_accents('ÁRVÍZTŰRŐ TÜKÖRFÚRÓGÉP')
    'ARVIZTURO TUKORFUROGEP'
    """
    # http://stackoverflow.com/questions/517923
    nkfd_form = unicodedata.normalize('NFKD', text)
    return "".join([c for c in nkfd_form if not unicodedata.combining(c)])


def remove_non_ascii(text):
    """
    >>> remove_non_ascii('László')
    'Lszl'
    """
    return ''.join(c for c in text if ord(c) < 128)


def strip_control_characters(text):
    """
    from http://chase-seibert.github.com/blog/2011/05/20/stripping-control-characters-in-python.html
    """
    if text:
        # unicode invalid characters
        RE_XML_ILLEGAL = '([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' +\
                         '|' +\
                         '([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' %\
                         (chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff),
                          chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff),
                          chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff))
        text = re.sub(RE_XML_ILLEGAL, "", text)

        # ascii control characters
        text = re.sub(r"[\x01-\x1F\x7F]", "", text)

    return text

#############################################################################

if __name__ == "__main__":
    text = "László"
    print(remove_accents(text))
    print(remove_non_ascii(text))
    print(strip_control_characters(text))
