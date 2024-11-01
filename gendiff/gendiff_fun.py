import json
import yaml


def open_file(curfile):
    if curfile[-5:] == ".json":
        with open(curfile) as file:
            file_inside = json.load(file)
    elif curfile[-5:] == ".yaml" or curfile[-4:] == ".yml":
        with open(curfile) as file:
            file_inside = yaml.safe_load(file)
    return file_inside


def generate_diff(first, second):
    stroka = '{'
    file1 = open_file(first)
    file2 = open_file(second)
    first_list_keys = list(file1.keys())
    second_list_keys = list(file2.keys())
    gen_list = list(set(list(file1.keys()) + list(file2.keys())))
    gen_list.sort()
    for el in gen_list:
        if el not in second_list_keys:
            if type(file1[el]) is bool:
                file1[el] = str(file1[el]).lower()
            stroka = stroka + '\n' + f'  - {str(el)}: {file1[el]}'
        elif el not in first_list_keys:
            print(el)
            if type(file2[el]) is bool:
                file2[el] = str(file2[el]).lower()
            stroka = stroka + '\n' + f'  + {str(el)}: {file2[el]}'
        elif file1[el] == file2[el]:
            if type(file1[el]) is bool:
                file1[el] = str(file1[el]).lower()
            stroka = stroka + '\n' + f'    {str(el)}: {file1[el]}'
        elif file1[el] != file2[el]:
            if type(file2[el]) is bool:
                file2[el] = str(file2[el]).lower()
            if type(file1[el]) is bool:
                file1[el] = str(file1[el]).lower()
            stroka = stroka + '\n' + f'  - {str(el)}: {file1[el]}'
            stroka = stroka + '\n' + f'  + {str(el)}: {file2[el]}'
    stroka = stroka + '\n' + '}'
    return str(stroka)
