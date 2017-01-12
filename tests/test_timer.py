# coding: utf-8

import time

from jplib.timer import Timer


def test_timer():
    timer = Timer()
    with timer:
        # Whatever you want to measure goes here
        time.sleep(0.1)

    assert 0.1 < timer.elapsed_time() < 0.2
