def generate_diff(first, second):
    stroka = '{'
    first_list = list(first.keys())
    second_list = list(second.keys())
    gen_list = list(set(list(first.keys()) + list(second.keys())))
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