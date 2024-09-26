import argparse


def generate_diff(first,second):
    stroka = '{'
    first_list = list(first.keys())
    second_list = list(second.keys())
    gen_list = list(set(list(first.keys())+list(second.keys())))
    gen_list.sort()
    for el in gen_list:
        if el not in second_list:
            stroka = stroka + '\n' + f'  - {str(el)}: {first[el]}'
        elif el not in first_list:
            stroka = stroka + '\n' + f'  + {str(el)}: {second[el]}'
        elif first[el] == second[el]:
            stroka = stroka + '\n' + f'    {str(el)}: {first[el]}'
        elif first[el] != second[el]:
            stroka = stroka + '\n' + f'  - {str(el)}: {first[el]}'
            stroka = stroka + '\n' + f'  + {str(el)}: {second[el]}'
    stroka = stroka + '\n' + '}'
    return stroka


def main():
    parser = argparse.ArgumentParser(description = 'Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f','--format', help='set format of output')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()