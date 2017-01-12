#!/usr/bin/env python3

"""
Hide and show the cursor.

# from jplib import cursor
"""

import os
import sys
from time import sleep


#===============================================================================
# CursorOff class
#     can be used in a with block
#     it will set cursor back ON, whatever happens
#===============================================================================

class CursorOff(object):
    def __enter__(self):
        off()

    def __exit__(self, *args):
        on()

#===============================================================================
# switch the cursor off/on
#===============================================================================

def off():
    """Hide cursor."""
    os.system('setterm -cursor off')


def on():
    """Show cursor."""
    os.system('setterm -cursor on')


def wait(sec, width=10):
    """
    Wait X seconds and refresh the countdown every second.

    width: number of characters to clear

    Return values:
    0 - OK, no interruption
    1 - countdown was interrupted
    """
    while sec > 0:
        sys.stdout.write(str(sec) + ' ' * width + '\r')
        sys.stdout.flush()
        sec -= 1
        try:
            sleep(1)
        except KeyboardInterrupt:
            print()
            return 1
    #
    return 0


def countdown_wait(sec, width=10):
    """
    Wait for X seconds and counts down.

    Return values:
    0 - OK, no interruption
    1 - countdown was interrupted
    """
    with CursorOff():
        return wait(sec, width)

#############################################################################

if __name__ == "__main__":
    print('# cursor on:')
    on()
    wait(3)
    print('# cursor off:')
    off()
    wait(3)
    on()
    print('# with cursorOff:')
    with CursorOff():
        wait(3)
    countdown_wait(5)
