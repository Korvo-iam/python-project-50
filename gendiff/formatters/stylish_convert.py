from .format_value import check_if_dic, format_value


def s_convert(dict_inside, tab='  '):  # noqa: C901
    stroka = ''
    oper_plus = '+ '
    oper_minus = '- '
    oper_neutral = '  '
    #skobka2 = ''
    #skobka1 = ''
    #oper = ''
    #inside = ''
    dict_inside = dict_inside['children']
    for elem in list(dict_inside):
        for key in elem:
            new_string = ''
            val = elem[key]
            if 'children' in val:
                skobka1 = '{'
                skobka2 = '}'
            status = val['status']
            if status == 'untouched':
                oper = oper_neutral
                old_val = val['old_value']
                inside = format_value(old_val)
                new_string = f'{tab}{oper}{key}: {inside}\n'
            elif status == 'nested':
                oper = oper_neutral
                inside = s_convert(val, tab=tab + '    ')
                skobka1 = '{'
                skobka2 = '}'
                new_string = (
                    f'{tab}{oper}{key}: {skobka1}\n'
                    f'{inside}{tab}  {skobka2}\n')
            elif status == 'added_dic':
                oper = oper_plus
                inside = s_convert(val, tab=tab + '    ')
                skobka1 = '{'
                skobka2 = '}'
                new_string = (
                    f'{tab}{oper}{key}: {skobka1}\n'
                    f'{inside}{tab}  {skobka2}\n')
            elif status == 'removed_dic':
                oper = oper_minus
                inside = s_convert(val, tab=tab + '    ')
                skobka1 = '{'
                skobka2 = '}'
                new_string = (
                    f'{tab}{oper}{key}: {skobka1}\n'
                    f'{inside}{tab}  {skobka2}\n')
            elif status == 'untouched_dic':
                oper = oper_neutral
                inside = s_convert(val, tab=tab + '    ')
                skobka1 = '{'
                skobka2 = '}'
                new_string = (
                f'{tab}{oper}{key}: {skobka1}\n'
                f'{inside}{tab}  {skobka2}\n')
            elif status == 'added' and check_if_dic(val):
                new_val = val['new_value']
                oper = oper_plus
                inside = format_value(new_val)
                new_string = f'{tab}{oper}{key}: {inside}\n'
            elif status == 'removed':
                oper = oper_minus
                old_val = val['old_value']
                inside = format_value(old_val)
                new_string = f'{tab}{oper}{key}: {inside}\n'
            elif status == 'changed':
                new_val = val['new_value']
                old_val = val['old_value']
                if check_if_dic(old_val):
                    old_val = s_convert(old_val, tab=tab + '    ')
                    skobka1 = '{'
                    skobka2 = '}'
                    old_val = f'{skobka1}\n{old_val}{tab}  {skobka2}'
                else:  # если статус был changed, и value это не словарь, 
                    # будет проверка на bool, None, и форматирование
                    old_val = format_value(old_val)
                if check_if_dic(new_val):
                    new_val = s_convert(new_val, tab=tab + '    ')
                    skobka1 = '{'
                    skobka2 = '}'
                    new_val = f'{skobka1}\n{new_val}{tab}  {skobka2}'
                else:
                    new_val = format_value(new_val)
                new_string = (
                f'{tab}{oper_minus}{key}: {old_val}\n'
                f'{tab}{oper_plus}{key}: {new_val}\n')
            stroka = stroka + new_string
    return stroka
