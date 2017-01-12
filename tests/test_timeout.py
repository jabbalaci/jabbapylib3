# coding: utf-8

import pytest
from jplib.timeout import Timeout, test_request


def test_timeout():
    with Timeout(3):
        test_request("OK")
    with Timeout(1):
        with pytest.raises(Timeout.Timeout):
            test_request("timeout occurs")
