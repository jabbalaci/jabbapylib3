#!/usr/bin/env python3
# encoding: utf-8

"""
What is my current desktop environment?

from http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment/21213358#21213358

# from jplib.desktop import desktop
"""

import os
import re
import subprocess
import sys

from jplib import process


def get_desktop_environment():
    #From http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment
    # and http://ubuntuforums.org/showthread.php?t=652320
    # and http://ubuntuforums.org/showthread.php?t=652320
    # and http://ubuntuforums.org/showthread.php?t=1139057
    if sys.platform in ["win32", "cygwin"]:
        return "windows"
    elif sys.platform == "darwin":
        return "mac"
    else: #Most likely either a POSIX system or something not much common
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session is not None: #easier to match if we don't have  to deal with caracter cases
            desktop_session = desktop_session.lower()
            if desktop_session in ["gnome", "unity", "cinnamon", "mate", "xfce4", "lxde", "fluxbox",
                                    "blackbox", "openbox", "icewm", "jwm", "afterstep","trinity", "kde"]:
                return desktop_session
            ## Special cases ##
            # Canonical sets $DESKTOP_SESSION to Lubuntu rather than LXDE if using LXDE.
            # There is no guarantee that they will not do the same with the other desktop environments.
            elif "xfce" in desktop_session or desktop_session.startswith("xubuntu"):
                return "xfce4"
            elif desktop_session.startswith("ubuntu"):
                return "unity"
            elif desktop_session.startswith("lubuntu"):
                return "lxde"
            elif desktop_session.startswith("kubuntu"):
                return "kde"
            elif desktop_session.startswith("razor"):  # e.g. razorkwin
                return "razor-qt"
            elif desktop_session.startswith("wmaker"):  # e.g. wmaker-common
                return "windowmaker"
        if os.environ.get('KDE_FULL_SESSION') == 'true':
            return "kde"
        elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
            if not "deprecated" in os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                return "gnome2"
        #From http://ubuntuforums.org/showthread.php?t=652320
        elif is_running("xfce-mcs-manage"):
            return "xfce4"
        elif is_running("ksmserver"):
            return "kde"
    # else
    return "unknown"


def is_running(process):
    #From http://www.bloggerpolis.com/2011/05/how-to-check-if-a-process-is-running-using-python/
    # and http://richarddingwall.name/2009/06/18/windows-equivalents-of-ps-and-kill-commands/
    try:  #Linux/Unix
        s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    except:  #Windows
        s = subprocess.Popen(["tasklist", "/v"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            return True
    #
    return False


def get_gnome_session_version():
    version = process.get_simple_cmd_output('gnome-session --version')
    return int(version.split()[1][0])    # main version number


env = get_desktop_environment()
if env == 'xfce4':
    if __name__ == "__main__": import xfce4 as d
    else: from . import xfce4 as d  # d stands for desktop
elif env == 'unity':
    try:
        ver = get_gnome_session_version()
    except IndexError:
        ver = 3

    if ver == 2:
        if __name__ == "__main__": import gnome2 as d
        else: from . import gnome2 as d
    elif ver == 3:
        if __name__ == "__main__": import gnome3 as d
        else: from . import gnome3 as d
    else:
        raise Exception('Warning! Your Gnome version is not supported. Send a pull request.')
else:
    raise Exception('Warning! Your desktop ({env}) is not supported. Send a pull request.'.format(env=env))


def set_wallpaper(img):
    d.set_wallpaper(img)


def get_wallpaper():
    return d.get_wallpaper()

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(get_wallpaper())
    else:
        img = sys.argv[1]
        set_wallpaper(img)
