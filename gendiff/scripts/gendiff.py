import argparse
from gendiff import gendiff_fun as g_f

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    result = g_f.generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == '__main__':
    main()
