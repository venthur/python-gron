import argparse

from gron import gron

parser = argparse.ArgumentParser()
parser.add_argument('file', help='A JSON file')


def main():
    args = parser.parse_args()
    with open(args.file, 'r') as fh:
        data = fh.read()
        print(gron(data))


if __name__ == '__main__':
    main()
