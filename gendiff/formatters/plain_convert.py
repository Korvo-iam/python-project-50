from .format_value import check_if_dic, format_value


def p_convert(dict_inside, path=''):  # noqa: C901
    def set_apostrophes(element):
        four_horsemen = ['true', 'false', 'null', '[complex value]']
        if element in four_horsemen or type(element) is int:
            element = element
        else:
            element = "'" + str(element) + "'"
        return element
    stroka = ''
    #inside = ''
    if path != '':
        dot = '.'
    else:
        dot = ''
    dict_inside = dict_inside['children']
    for elem in list(dict_inside):
        for key in elem:
            new_string = ''
            val = elem[key]
            status = val['status'] 
            current_path = path + dot + key
            if status == 'nested':
                inside = p_convert(val, current_path)
                new_string = f'{inside}'
            elif status == 'added_dic':
                inside = '[complex value]'
                new_string = (
                    f"Property '{current_path}' "
                    f"was added with value: {inside}\n")
            elif status == 'removed_dic':
                inside = '[complex value]'
                new_string = f"Property '{current_path}' was removed\n"
            elif status == 'removed':
                new_string = f"Property '{current_path}' was removed\n"
            elif status == 'added':
                new_val = val['new_value']
                inside = format_value(new_val)
                inside = set_apostrophes(inside)
                new_string = (
                    f"Property '{current_path}' "
                    f"was added with value: {inside}\n")
            elif status == 'changed':
                new_val = val['new_value']
                old_val = val['old_value']
                if check_if_dic(old_val):
                    old_val = '[complex value]'
                else:
                    old_val = format_value(old_val)
                if check_if_dic(new_val):
                    new_val = '[complex value]'
                else:
                    new_val = format_value(new_val)
                old_val = set_apostrophes(old_val)
                new_val = set_apostrophes(new_val)
                new_string = (
                    f"Property '{current_path}' was updated. "
                    f"From {old_val} to {new_val}\n")
            stroka = stroka + new_string
    return stroka
