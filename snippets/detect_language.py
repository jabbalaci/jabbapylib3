#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
using textblob
"""

from langdetect import detect

TEXT = """
Amikor ismeretlenek elrabolják Thuviát, Ptarth hercegnőjét, Carthoris,
a Mars urának fia az első számú gyanúsított. És csakis Carthoris
mentheti meg a leányt, aki szerelmet ültetett a szívébe.
"""


def get_lang(text):
    return detect(text)

#############################################################################

if __name__ == "__main__":
    print(get_lang(TEXT))
