# coding: utf-8

import re

import ipaddress
import pytest

from jplib import network

IP = None


def setup_module(module):
    """runs just once per module"""
    global IP
    IP = network.get_my_external_ip()

#############################################################################

def test_is_internet_on():
    if IP:
        assert network.is_internet_on(method=1)
        assert network.is_internet_on(method=2)
        assert network.is_internet_on(method=3)
    else:
        assert not network.is_internet_on(method=1)
        assert not network.is_internet_on(method=2)
        assert not network.is_internet_on(method=3)


def test_get_my_external_ip():
    if IP:
        try:
            res = ipaddress.ip_address(IP)
            assert isinstance(res, ipaddress.IPv4Address) or isinstance(res, ipaddress.IPv6Address)
        except ValueError:
            pytest.fail("invalid IP address")
    else:
        assert IP is None

#############################################################################

def test_ping():
    val = network.ping('www.google.com')
    if IP:
        assert val > 0.0
    else:
        assert val is None


def test_fping():
    val = network.fping('www.google.com')
    if IP:
        assert val > 0.0
    else:
        assert val is None
