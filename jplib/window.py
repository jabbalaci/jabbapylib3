#!/usr/bin/env python3

"""
Find a window by its name, get its window ID, bring it to foreground, etc.

required package: xdotool (sudo apt-get install xdotool)

# from jplib import window
"""

import os
import re
from collections import OrderedDict

from six import StringIO

from jplib import fs, process
from jplib.process import get_simple_cmd_output


def get_window_title_by_id(wid):
    assert fs.which("xwininfo"), "the program xwininfo was not found."
    #
    result = get_simple_cmd_output('xwininfo -id {id}'.format(id=wid))
    for line in StringIO(result):
        line = line.encode('ascii', 'ignore').decode('ascii').rstrip("\n")
        match = re.search(r'^xwininfo: Window id:.*"(.*)"$', line)
        if match:
            return match.group(1)
    #
    return None


def get_active_window_id(hexa=False):
    """
    Window ID of the active window.

    The return value is a string. By default, the ID is in decimal
    format. If hexa is True, the return value is hexadecimal.
    In both cases, the return value is a string.
    """
    assert fs.which("xdotool"), "the program xdotool was not found."
    #
    wid = get_simple_cmd_output('xdotool getactivewindow').strip()
    if not hexa:
        return wid
    else:
        return hex(int(wid))


def activate_window_by_id(wid):
    """
    Put the focus on and activate the the window with the given ID.
    """
    assert fs.which("xdotool"), "the program xdotool was not found."
    #
    os.system('xdotool windowactivate {wid}'.format(wid=wid))


def toggle_fullscreen(wid_hexa):
    """
    Toggle the given window to fullscreen.

    The window id is a hexa string.
    """
    assert fs.which("wmctrl"), "the program wmctrl was not found."
    #
    cmd = "wmctrl -i -r {wid} -b toggle,maximized_vert,maximized_horz".format(wid=wid_hexa)
    os.system(cmd)


def print_wmctrl_output():
    """
    Print the output of wmctrl.
    """
    assert fs.which("wmctrl"), "the program wmctrl was not found."
    #
    cmd = "wmctrl -lGpx"
    os.system(cmd)


def get_wmctrl_output():
    """
    Parses the output of wmctrl and returns a list of ordered dicts.
    """
    assert fs.which("wmctrl"), "the program wmctrl was not found."
    #
    cmd = "wmctrl -lGpx"
    lines = [line for line in process.get_simple_cmd_output(cmd)
                                     .encode('ascii', 'ignore')
                                     .decode('ascii').split("\n") if line]

    res = []
    for line in lines:
        pieces = line.split()
        d = OrderedDict()
        #d['wid'] = int(pieces[0], 16)  # converted to decimal
        d['wid'] = pieces[0]
        d['desktop'] = int(pieces[1])
        d['pid'] = int(pieces[2])
        d['geometry'] = [int(x) for x in pieces[3:7]]
        d['window_class'] = pieces[7]
        d['client_machine_name'] = pieces[8]
        d['window_title'] = ' '.join(pieces[9:])
        res.append(d)
    #
    return res


def get_wid_by_pid(pid):
    """
    Having a pid, return its wid.

    We have the PID of a process. Figure out its window ID.
    """
    for d in get_wmctrl_output():
        if d['pid'] == pid:
            return d['wid']
    #
    return None


def get_wid_by_title(title_regexp):
    """
    Having the window title (as a regexp), return its wid.

    If not found, return None.
    """
    for d in get_wmctrl_output():
        m = re.search(title_regexp, d['window_title'])
        if m:
            return d['wid']
    #
    return None


def switch_to_window(title_regexp):
    wid = get_wid_by_title(title_regexp)
    if wid:
        print('# window id:', wid)
        wid = int(wid, 16)
        print('# switching to the other window')
        activate_window_by_id(wid)
    else:
        print('# not found')


def interactive_switch():
    """
    Ask the title of a window and switch to it.

    It's enough to specify just a substring of the title.
    This method is just an interactive demo of the window
    switching feature.
    """
    title = raw_input('substring in title> ').strip()
    switch_to_window(title)

#############################################################################

if __name__ == "__main__":
    interactive_switch()
#    wid = get_active_window_id()
#    print(wid)
#    wid_hexa = get_active_window_id(hexa=True)
#    print(wid_hexa)
#    activate_window_by_id(wid)
#    print(get_window_title_by_id(wid))
##    toggle_fullscreen(wid_hexa)
#    print(get_wmctrl_output())
#    print(get_wid_by_pid(2347))
