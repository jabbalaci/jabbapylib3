#!/usr/bin/env python3

"""
A skeleton file for scraping.
"""
import sys

if __name__ == "__main__":
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from jplib.scraper import bsoup as bs
from jplib.web import get_page


def process(url):
    html = get_page(url)
    soup = bs.to_soup(html)
    print(soup)


def main(argv):
    if len(argv) == 1:
        print("Usage: {} <URL>".format(argv[0]))
        sys.exit(1)
    # else
    process(argv[1])

##############################################################################

if __name__ == "__main__":
    main(sys.argv)
