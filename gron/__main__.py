import sys

from gron.gron import gron


def main():
    with(open(sys.argv[1], 'r')) as fh:
        data = fh.read()
        print(gron(data))


if __name__ == '__main__':
    main()
