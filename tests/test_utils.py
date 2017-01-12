# coding: utf-8

from jplib import utils


def test_my_shuffle():
    array = [1, 2, 3]
    assert len(utils.my_shuffle(array)[::-1]) == 3
    last = utils.my_shuffle(array)[-1]
    assert 1 <= last <= 3


def test_inc_string():
    assert utils.inc_string('a') == 'b'
    assert utils.inc_string('f') == 'g'
    assert utils.inc_string('z') == 'aa'
    assert utils.inc_string('zz') == 'aaa'
    assert utils.inc_string('af') == 'ag'
    assert utils.inc_string('ajhfsdhgf') == 'ajhfsdhgg'
    assert utils.inc_string('ajhfsdhgz') == 'ajhfsdhha'


def test_pretty_num():
    assert utils.pretty_num(1977) == '1,977'
    assert utils.pretty_num(-1977) == '-1,977'
    #
    assert utils.pretty_num(1234567) == '1,234,567'
    assert utils.pretty_num(-1234567) == '-1,234,567'
    #
    assert utils.pretty_num(123) == '123'
    assert utils.pretty_num(-123) == '-123'


def test_sizeof_fmt():
    assert utils.filesize_fmt(23) == '23.0 b'
    assert utils.filesize_fmt(1234) == '1.2 KB'
    assert utils.filesize_fmt(1234567) == '1.2 MB'
    assert utils.filesize_fmt(1234567890) == '1.1 GB'
    assert utils.filesize_fmt(1234567890123) == '1.1 TB'
    assert utils.filesize_fmt(123456789012357) == '112.3 TB'
