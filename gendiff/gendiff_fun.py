import json


def generate_diff(first, second):
    with open(first) as file1:
        json_inside1 = json.load(file1)
    with open(second) as file2:
        json_inside2 = json.load(file2)
    stroka = '{'
    file1 = json_inside1
    file2 = json_inside2
    first_list = list(file1.keys())
    second_list = list(file2.keys())
    gen_list = list(set(list(file1.keys()) + list(file2.keys())))
    gen_list.sort()
    for el in gen_list:
        if el not in second_list:
            if type(file1[el]) is bool:
                file1[el] = str(file1[el]).lower()
            stroka = stroka + '\n' + f'  - {str(el)}: {file1[el]}'
        elif el not in first_list:
            if type(file2[el]) is bool:
                file2[el] = str(file2[el]).lower()
            stroka = stroka + '\n' + f'  + {str(el)}: {file2[el]}'
        elif file1[el] == file2[el]:
            stroka = stroka + '\n' + f'    {str(el)}: {file1[el]}'
        elif file1[el] != file2[el]:
            stroka = stroka + '\n' + f'  - {str(el)}: {file1[el]}'
            stroka = stroka + '\n' + f'  + {str(el)}: {file2[el]}'
    stroka = stroka + '\n' + '}'
    return stroka
