import argparse
from gendiff import gendiff_fun


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')
    args = parser.parse_args()
    result = gendiff_fun.generate_diff(args.first_file, args.second_file, format_name=args.format)
    print(result)


if __name__ == '__main__':
    main()
