# coding: utf-8

from jplib import config as cfg
from jplib import jhash

FILE = cfg.TEST_ASSETS_DIR + '/text.txt'


def test_string_to_md5():
    assert jhash.string_to_md5('uncrackable12') == '7e1f843673a0c8082378a0f7e6831c7b'


def test_file_to_md5():
    res = jhash.file_to_md5(FILE)
    assert res == '7565a01bd35f31ba82ab55c978c1b755'


def test_get_random_string():
    res = jhash.get_random_string()
    assert len(res) == 12 and res.isalnum()
    #
    res2 = jhash.get_random_string()
    assert res != res2


def test_get_secret_key():
    res = jhash.get_secret_key()
    assert len(res) == 50
    #
    res2 = jhash.get_secret_key()
    assert res != res2


def test_str2num_and_num2str():
    s = jhash.get_secret_key()
    assert jhash.num2str(jhash.str2num(s)) == s
    #
    s = "hello world"
    assert jhash.num2str(jhash.str2num(s)) == s


def test_str_to_base64_and_base64_to_str():
    to = jhash.str_to_base64
    back = jhash.base64_to_str
    #
    assert back(to("something")) == "something"
    assert to(back("TMOhc3psw7M=")) == "TMOhc3psw7M="
