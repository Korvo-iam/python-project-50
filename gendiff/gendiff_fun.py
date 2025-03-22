import json
import yaml

def open_file(curfile):
    if isinstance(curfile, dict):
        file_inside = curfile
        return file_inside
    elif curfile[-5:] == ".json":
        with open(curfile) as file:
            file_inside = json.load(file)
    elif curfile[-5:] == ".yaml" or curfile[-4:] == ".yml":
        with open(curfile) as file:
            file_inside = yaml.safe_load(file)
    return file_inside

def set_recursive_untouched(dict):
    if check_if_dic(dict):
        new_dic = {}
        for key in dict:
            val = dict[key]
            if check_if_dic(val):
                val = set_recursive_untouched(val)
            else:
                dict['status'] = 'untouched'
    return dict

def set_status(dic1, dic2, deepnees=0):
    list1 = sorted(list(set(list(dic1.keys()) + list(dic2.keys()))))
    dictionary = {}
    children = []
    children_main = []
    if deepnees == 0:
        status = 'root'
        key = 'root'
        children_main.append(set_status(dic1,dic2, deepnees=deepnees+1))
        value = {"status": status, "children": children_main}
        dictionary[key]=value
        return dictionary
    else:
        for key in list1:
            if key in dic1 and check_if_dic(dic1[key]) or key in dic2 and check_if_dic(dic2[key]):#если ключ в словаре1 и его значение - словарь, или если ключ в словаре2 и его значение - словарь
                if key in dic1 and key not in dic2:#если ключ в словаре1, но не в словаре2
                    status = 'removed'
                    value = {'status':status, 'old_value':dic1[key], 'new_value':{}}
                elif key in dic2 and key not in dic1:#если ключ в словаре2, но не словаре1
                    status = 'added'
                    #val = set_recursive_untouched(dic2[key])
                    val = dic2[key]
                    value = {'status':status, 'old_value':{}, 'new_value':val}
                elif key in dic1 and key in dic2 and not check_if_dic(dic1[key]) or not check_if_dic(dic2[key]):#если ключ в словаре1 и словаре2, где 1 из случаев - его значение - не словарь
                    status = 'changed'
                    value = {'status':status, 'old_value':dic1[key], 'new_value':dic2[key]}
                else :
                    status='nested'
                    if key in dic1 and check_if_dic(dic1[key]):
                        if key in dic2 and check_if_dic(dic2[key]):
                            children.append(set_status(dic1[key], dic2[key], deepnees = deepnees + 1))
                        else:
                            children.append(set_status(dic1[key], {}, deepnees = deepnees + 1))
                    elif key not in dic1:
                        if key in dic2 and check_if_dic(dic2[key]):
                            children.append(set_status({}, dic2[key], deepnees = deepnees + 1))
                    value = {'status':status,'children':children}
                dictionary[key]=value
                children=[]
            else:
                if key not in dic1:
                    status = 'added'
                    old_value = None
                    new_value = dic2[key]
                elif key not in dic2:
                    status = 'removed'
                    old_value = dic1[key]
                    new_value = None
                elif dic1[key] != dic2[key]:
                    status = 'changed'
                    old_value = dic1[key]
                    new_value = dic2[key]
                    if check_if_dic(dic1[key]):
                        if check_if_dic(dic2[key]):
                            old_value = set_status(dic1[key], dic2[key], deepnees=deepnees+1)
                            new_value = set_status(dic2[key], dic1[key], deepnees=deepnees+1)
                else:
                    status = 'untouched'
                    old_value = dic1[key]
                    new_value = None
                value = {"status": status, "old_value": old_value, "new_value": new_value}
                dictionary[key]=value
    return dictionary

def make_dic_structure(dict, skobka1, skobka2, tab=' '):
    inside = ''
    skobka1 ='{'
    skobka2 = '}'
    tab = tab + '  '
    if check_if_dic(dict):
        for key in dict:
            print(f'keyekeyeyeyeyeyeyeyyyeyyeyeyeyeye : {key}')
            val = dict[key]
            if check_if_dic(val):
                val = make_dic_structure(val, skobka1=skobka1, skobka2=skobka2, tab=tab+tab)
            newstring = f'{skobka1}\n{tab+ "   "}{key}: {val}\n{tab}{skobka2}'
        inside = inside + newstring
    return inside



def n_convert(dict_inside, tab=' '):
    print(f'>>>>\n{dict_inside}\n<<<<<<<<')
    stroka = ''
    a = ''
    oper_plus = '+ '
    oper_minus = '- '
    oper_neutral = '  '
    skobka2 = ''
    skobka1 = ''
    oper = ''
    inside = ''
    dict_inside = dict_inside['children']
    for elem in list(dict_inside):
        for key in elem:
            a = a + key
            new_string = ''
            val = elem[key]
            if_dic = False
            if check_if_dic(val):
                if_dic = True
            if 'children' in val:
                skobka1 = '{'
                skobka2 = '}'
            status = val['status']
            if status == 'untouched':
                oper = oper_neutral
                old_val = val['old_value']
                if old_val is None:
                    inside = "null"
                else:
                    inside = str(old_val)
                new_string = f'{tab}{oper}{key}: {inside}\n'
            elif status == 'nested':
                oper = oper_neutral
                inside = n_convert(val, tab=tab + '  ')
                skobka1 = '{'
                skobka2 = '}'
                new_string = f'{tab}{oper}{key}: {skobka1}\n{inside}{tab}{skobka2}\n'
            elif status == 'added' and check_if_dic(val):
                new_val = val['new_value']
                oper = oper_plus
                if new_val is None:
                    inside = "null"
                else:
                    inside = str(new_val)
                new_string = f'{tab}{oper}{key}: {inside}\n'
            elif status == 'removed':
                oper = oper_minus
                old_val = val['old_value']
                if old_val is None:
                    inside = "null"
                else:
                    inside = str(old_val)
                    print(f'>>>{inside}')
                new_string = f'{tab}{oper}{key}: {inside}\n'
            elif status == 'changed':
                new_val = val['new_value']
                old_val = val['old_value']
                new_string = f'{tab}{oper_minus}{key}: {old_val}\n{tab}{oper_plus}{key}: {new_val}\n'
            stroka = stroka + new_string
    print('***')
    #print(stroka)
    return stroka


def low(element):
    if check_if_dic(element):
        #print(element)
        if 'status' in element:
            del element['status']
    if isinstance(element, bool):
        element = str(element).lower()
    elif isinstance(element, type(None)):
        element = 'null'
    return element


def check_if_dic(element):
    return isinstance(element, dict)


def generate_diff(first, second):
    diff = {}
    if first is dict:
        file1 = first
    else:
        file1 = open_file(first)
    if second is dict:
        file2 = second
    else:
        file2 = open_file(second)
    diff = set_status(file1,file2)
    diff_inside = diff['root']
    fin_string = '{\n'
    #print(type(diff_inside))
    fin_string += n_convert(diff_inside) + '\n}'
    return fin_string


path1 = "file7.json"
path2 = "file8.json"
b = generate_diff(path1,path2)


print('////')
print('-------------------\n')
print(b)
print('\n-------------------')