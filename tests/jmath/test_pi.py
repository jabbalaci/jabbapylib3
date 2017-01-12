# coding: utf-8

import os

from jplib.jmath import pi

##############################################################################

def setup_module(module):
    """ download the data file """
    pi.get_digits_of(pi.PI3)

def teardown_module(module):
    """ delete the data file """
    os.unlink(pi.TMP_DIR + '/' + pi.PI3)

##############################################################################

# 1st part
def test_get_digits_of():
    digits = pi.get_digits_of(pi.PI3)
    assert len(digits) == 1000
    assert digits[:10] == '1415926535'
    assert digits[-10:] == '2164201989'


# 2nd part
def test_get_digits():
    etalon = pi.get_digits_of(pi.PI3)[:200]
    result = pi.get_digits(200)
    assert result == etalon


# 3rd part
#def test_get_pi():
#    etalon = pi.get_digits(200)
#    result = pi.get_pi(200)
#    assert result == etalon


# 4th part
#def test_get_pi_with_bigfloat():
#    # the last digit is rounded in both cases,
#    # so it's cut off
#    etalon = pi.get_pi(181)[:-1]
#    result = pi.get_pi_with_bigfloat(600)[:-1]
#    assert result == etalon
