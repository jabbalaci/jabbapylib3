# coding: utf-8

"""
Write something to:
* stderr
* stdout
And exit with a code.
"""

import sys


def main():
    sys.stdout.write("árvíztűrő tükörfúrógép")
    sys.stderr.write("stderr")
    sys.exit(3)

##############################################################################

if __name__ == "__main__":
    main()
