#!/usr/bin/env python3

"""
Extract Firefox cookies
=======================

This script extracts cookies from Firefox's cookies.sqlite file
that are specific to a given host. The exported cookies are saved
in the file cookies.txt.

Then, you can use this exported file with wget to download content
that require authentication via cookies:

wget --cookies=on --load-cookies=cookies.txt --keep-session-cookies "http://..."

The original script was written by Dirk Sohler:
https://old.0x7be.de/2008/06/19/firefox-3-und-cookiestxt/

This version is a bit refactored but does exactly the same.
Website: https://ubuntuincident.wordpress.com/2011/09/05/download-pages-with-wget-that-are-protected-by-cookies/
GitHub:  https://github.com/jabbalaci/Bash-Utils (see the firefox/ folder)

Last update: 2017-05-17 (yyyy-mm-dd)
"""

import os
import sqlite3 as db
import sys
from io import StringIO
from pathlib import Path

from http.cookiejar import Cookie, LWPCookieJar

FIREFOX_DIR = Path(os.path.expanduser('~'), '.mozilla', 'firefox')
OUTPUT = 'cookies.txt'
CONTENTS = "host, path, isSecure, expiry, name, value"


def get_cookie_db_path(firefox_dir):
    for e in os.listdir(firefox_dir):
        if e.endswith('.default'):
            p = Path(firefox_dir, e, 'cookies.sqlite')
            if not p.is_file():
                print("Error: the file '{0}' doesn't exist".format(str(p)), file=sys.stderr)
                sys.exit(1)
            else:
                return str(p)
    # else
    print("Error: the user dir. was not found in '{0}'".format(firefox_dir), file=sys.stderr)
    sys.exit(1)


def extract(host):
    cookie_db = get_cookie_db_path(str(FIREFOX_DIR))
    print("# working with", cookie_db)

    conn = db.connect(cookie_db)
    cursor = conn.cursor()

    sql = "SELECT {c} FROM moz_cookies WHERE host LIKE '%{h}%'".format(c=CONTENTS, h=host)
    cursor.execute(sql)

    out = open(OUTPUT, 'w')
    cnt = 0
    for row in cursor.fetchall():
        s = "{0}\tTRUE\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(row[0], row[1],
                 str(bool(row[2])).upper(), row[3], str(row[4]), str(row[5]))
        out.write(s)
        cnt += 1

    print("Search term: {0}".format(host))
    print("Exported: {0}".format(cnt))

    out.close()
    conn.close()


def get_cookies_in_text(host):
    """Export cookies in plain-text (like cookies.txt) format.

    Return value: exported cookies as a string."""
    cookie_db = get_cookie_db_path(str(FIREFOX_DIR))
    conn = db.connect(cookie_db)
    cursor = conn.cursor()

    sql = "SELECT {c} FROM moz_cookies WHERE host LIKE '%{h}%'".format(c=CONTENTS, h=host)
    cursor.execute(sql)

    out = StringIO()
    for row in cursor.fetchall():
        try:
            s = "{0}\tTRUE\t{1}\t{2}\t{3}\t{4}\t{5}".format(row[0], row[1],
                     str(bool(row[2])).upper(), row[3], str(row[4]), str(row[5]))
            print(s, file=out)
        except UnicodeEncodeError:
            print("Warning: UnicodeEncodeError:", file=sys.stderr)
            print(row, file=sys.stderr)

    value = out.getvalue().strip()
    out.close()
    conn.close()

    return value


def get_cookies_in_cookiejar(host):
    """Export cookies and put them in a cookiejar.

    Return value: a cookiejar filled with cookies."""
    # based on http://www.guyrutenberg.com/2010/11/27/building-cookiejar-out-of-firefoxs-cookies-sqlite/
    cj = LWPCookieJar()       # This is a subclass of FileCookieJar that has useful load and save methods

    cookie_db = get_cookie_db_path(str(FIREFOX_DIR))
    conn = db.connect(cookie_db)
    cursor = conn.cursor()
    sql = "SELECT {c} FROM moz_cookies WHERE host LIKE '%{h}%'".format(c=CONTENTS, h=host)
    cursor.execute(sql)

    for item in cursor.fetchall():
        c = Cookie(0, item[4], item[5],
            None, False,
            item[0], item[0].startswith('.'), item[0].startswith('.'),
            item[1], False,
            item[2],
            item[3], item[3]=="",
            None, None, {})
        #print c
        cj.set_cookie(c)

    return cj


if __name__ == "__main__":
    # if len(sys.argv) == 1:
    #     print("{0}: specify the host".format(Path(sys.argv[0]).name))
    #     sys.exit(1)
    # # else
    # extract(sys.argv[1])
    host = "steampowered.com"
    print(get_cookies_in_cookiejar(host))
