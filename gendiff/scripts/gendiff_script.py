import argparse

from .generate_diff import generate as g_f


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')
    args = parser.parse_args()
    diff = g_f(
        first=args.first_file,
        second=args.second_file,
        format_name=args.format)
    print(diff)


if __name__ == '__main__':
    main()
