"""Gron's command line interface (CLI).


Attributes
----------
parser : argparse.ArgumentParser

"""

import argparse
import sys

from gron import gron


parser = argparse.ArgumentParser()
parser.add_argument(
    'file',
    help='A JSON file, if not given gron reads from STDIN',
    nargs='?',
    type=argparse.FileType('r'),
    default=sys.stdin)


def main():
    """Gron's CLI

    This method reads the arguments for the command line interface and
    runs `gron`.

    """
    args = parser.parse_args()
    data = args.file.read()
    print(gron(data))


if __name__ == '__main__':
    main()
