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
    args = parser.parse_args()
    data = args.file.read()
    print(gron(data))


if __name__ == '__main__':
    main()
