# coding: utf-8

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import detect_language as dl

HU = """
Amikor ismeretlenek elrabolják Thuviát, Ptarth hercegnőjét, Carthoris,
a Mars urának fia az első számú gyanúsított. És csakis Carthoris
mentheti meg a leányt, aki szerelmet ültetett a szívébe.
"""

EN = """
One line is read from the standard input, or from the file descriptor
supplied as an argument to the -u option. The first word of the line is
assigned to the first name, NAME1, the second word to the second name, and
so on, with leftover words and their intervening separators assigned to
the last name, NAMEN. If there are fewer words read from the input stream
than there are names, the remaining names are assigned empty values.
"""


def test_detect_language():
    assert dl.get_lang(HU) == "hu"
    assert dl.get_lang(EN) == "en"
