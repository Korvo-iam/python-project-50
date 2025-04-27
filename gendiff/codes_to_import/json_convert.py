from .format_value import format_value, check_if_dic, transform_var_json


def json_convert(dict_inside, tab='    ', comma = ''):
    no_changes_statuses = ['nested','added_dic','removed_dic', 'untouched_dic']
    stroka = ''
    skobka2 = ''
    skobka1 = ''
    inside = ''
    children_string = ''
    new_val_string = ''
    old_val_string = ''
    status_string = ''
    new_val_comma = ''
    newline='\n'
    dict_inside = dict_inside['children']
    for elem in list(dict_inside):
        for key in elem:
            new_string = ''
            val = elem[key]
            skobka1 = '{'
            skobka2 = '}'
            key =  transform_var_json(key)
            key_string = f'{tab}{key}:'
            tab = tab + '    '
            #print(key)
            #print(val)
            status = val['status']
            formated_status = transform_var_json(status)+','
            if status in no_changes_statuses:
                skobka3 = '['
                skobka4 = ']'
                children = json_convert(val, tab=tab+'    ', comma=',')
                #print(key)
                if children.endswith(",\n"):
                    children = children[:-2]+newline
                children_string = f'{tab}"children": {skobka3}{newline}{tab}{skobka1}{newline}{children}{tab}{skobka2}{newline}{tab[:-2]}{skobka4}{newline}'
            if 'old_value' in val:
                old_val = val['old_value']
                if check_if_dic (old_val):
                    #print('TRUE')
                    if 'status' in old_val:
                        if old_val['status'] in no_changes_statuses:
                            #print('TRUE')
                            #print(old_val)
                            #print(old_val['status'])
                            ov_children = json_convert(old_val,tab = tab + '    ')
                            ov_status = transform_var_json(old_val['status'])
                            #converted_old_val = json_convert(old_val, tab=tab + '  ', comma=',')
                            #old_val_string = f'{tab}"old_value": {{\n{converted_old_val}{tab}}},{newline}'
                            #print('>>>')
                            #print(f'{tab}"status": {ov_status}\n{tab}"children": [\n{tab}{ov_children}\n]')
                            #print('<<<')
                            old_val = f'{tab}    "status": {ov_status},\n{tab}    "children": [\n{tab}{skobka1}\n{ov_children[:-2]}{skobka2}\n{tab}  ]'
                            #print(old_val_string)
                            #print('<<<<')
                            old_val_string = f'{tab}"old_value": {skobka1}\n{old_val}\n{tab}{skobka2},{newline}'
                            #old_val_string = f'{tab}"old_value": {skobka1}\n{old_val}{skobka2},{newline}'
                            #old_val_string = f'{tab}"status": {ov_status}{newline}{tab}{skobka1}{newline}"children: "{ov_children}{tab}{skobka2}{newline}{tab[:-2]}{newline}'
                            #print('>>>', old_val_string,'<<<')
                            #if old_val_string.endswith(",\n"):
                            #    children = children[:-2]+newline
                        #print('>>>>>')
                        #print(old_val_string[-2:])
                        #print('<<<<<')
                        if old_val_string.endswith(",\n"):
                            print(True)
                            old_val_string = old_val_string[:-2]+'\n'
                    else :
                       old_val_string = f'{tab}"old_value": {newline}{tab}{skobka1}{newline}{old_val}{tab}{skobka2}{newline}'
                else:
                   old_val = transform_var_json(old_val)
                   old_val_string = f'{tab}"old_value": {old_val},{newline}'
            if 'new_value' in val:
                new_val = val['new_value']
                if check_if_dic (new_val):
                    new_val = newline + json_convert(new_val, tab=tab+'', comma=',')
                else:
                    new_val = transform_var_json(new_val)
                if len(children_string)>1:
                    new_val_comma = ','
                new_val_string = f'{tab}"new_value": {new_val}{new_val_comma}{newline}'
            if status in no_changes_statuses:
                old_val_string = ''
                new_val_string = ''
            status_string = f'{tab}"status": {formated_status}{newline}'
            tab = tab[:-4]
            inside = f'{skobka1}\n{status_string}{old_val_string}{new_val_string}{children_string}{tab}{skobka2}{comma}\n'
            new_string = f'{key_string} {inside}'

            inside = ''
            children_string = ''
            new_val_string = ''
            old_val_string = ''
            status_string = ''
            new_val_comma = ''
            stroka = stroka + new_string
    print(stroka)
    return stroka


