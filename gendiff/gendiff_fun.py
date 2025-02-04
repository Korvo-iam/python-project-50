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


def convert_if_d(element, newline='\n', tab='\t'):
    if check_dic(element):
        stroka = ''
        skobka1='{'
        skobka2='}'
        print(f'element : {element}')
        for key in element:
            print(key)
            val = element[key]
            if check_dic(val):
                print('bas')
                val = convert_if_d(val, tab=tab+tab)
            else :
                
                val = val
            otstup = newline+tab
            stroka += f'{otstup}{key}: {skobka1}{otstup}{val}{otstup}{skobka2}'
        return stroka
    else:
        print(f'will be same : {element}')
        print(element)
        return element


def convert_if_added(dictionary):
    stroka=''
    for key in dictionary.keys():
        global_key = key
        working_dic = dictionary[key]
        status = working_dic['status']
        if status == 'added':
            oper = '+'
            working_dic = working_dic['new_value']
            stroka += f"\n{oper} {global_key}: "
            stroka += '{'
            for key in working_dic:
                val = working_dic[key]
                print(f'will be converted : {val}')
                val = convert_if_d(val)
                print(f'val : {val}')
                stroka += f"\n\t{key}: {low(val)}"
    print(stroka)
    return stroka


def convert_if_removed(dictionary):
    stroka = "{"
    for key in dictionary.keys():
        global_key = key
        working_dic = dictionary[key]
        status = working_dic['status']
        if status == 'removed':
            oper = '-'
            working_dic = working_dic['old_value']
            skobka = '{'
            stroka += f"\n{oper} {global_key}: {skobka}"
            for key in working_dic:
                val = working_dic[key]
                stroka += f"\n\t{key}: {low(val)}"
    stroka = stroka + '\n}'
    return stroka


def check_status(dic1, dic2, deepnees=0):
    list1 = sorted(list(set(list(dic1.keys()) + list(dic2.keys()))))
    print(f'lilililililililililililili\n{list1}\nlilililililililililililili')
    dictionary = {}
    children = []
    children_main = []
    if deepnees == 0:
        status = 'root'
        key = 'root'
        children_main.append(check_status(dic1,dic2, deepnees=deepnees+1))
        value = {"status": status, "children": children_main}
        dictionary[key]=value
        return dictionary
    else:
        for key in list1:
            if key in dic1 and check_dic(dic1[key]) or key in dic2 and check_dic(dic2[key]):
                if key in dic1 and key not in dic2:
                    status = 'removed'
                    value = {'status':status, 'old_value':dic1[key], 'new_value':{}}
                elif key in dic2 and key not in dic1:
                    status = 'added'
                    value = {'status':status, 'old_value':{}, 'new_value':dic2[key]}
                else :
                    status='nested'
                    if key in dic1 and check_dic(dic1[key]):
                        if key in dic2 and check_dic(dic2[key]):
                            children.append(check_status(dic1[key], dic2[key], deepnees = deepnees + 1))
                        else:
                            children.append(check_status(dic1[key], {}, deepnees = deepnees + 1))
                    elif key not in dic1:
                        if key in dic2 and check_dic(dic2[key]):
                            children.append(check_status({}, dic2[key], deepnees = deepnees + 1))
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
                    if check_dic(dic1[key]):
                        if check_dic(dic2[key]):
                            old_value = check_status(dic1[key], dic2[key], deepnees=deepnees+1)
                            new_value = check_status(dic2[key], dic1[key], deepnees=deepnees+1)
                else:
                    status = 'untouched'
                    old_value = dic1[key]
                    new_value = None
                value = {"status": status, "old_value": old_value, "new_value": new_value}
                dictionary[key]=value
    return dictionary


def check_status_2(dic1, dic2, deepnees=0):
    list1 = sorted(list(set(list(dic1.keys()) + list(dic2.keys()))))
    #print(f'lilililililililililililili\n{list1}\nlilililililililililililili')
    dictionary = {}
    children = []
    children_main = []
    if deepnees == 0:
        status = 'root'
        key = 'root'
        children_main.append(check_status(dic1,dic2, deepnees=deepnees+1))
        value = {"status": status, "children": children_main}
        dictionary[key]=value
        return dictionary
    else:
        for key in list1:
            if key in dic1 and check_dic(dic1[key]) or key in dic2 and check_dic(dic2[key]):
                status='nested'
                if key in dic1 and check_dic(dic1[key]):
                    if key in dic2 and check_dic(dic2[key]):
                        children.append(check_status(dic1[key], dic2[key], deepnees = deepnees + 1))
                    else:
                        children.append(check_status(dic1[key], {}, deepnees = deepnees + 1))
                elif key not in dic1:
                    if key in dic2 and check_dic(dic2[key]):
                        children.append(check_status({}, dic2[key], deepnees = deepnees + 1))
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
                    if check_dic(dic1[key]):
                        if check_dic(dic2[key]):
                            old_value = check_status(dic1[key], dic2[key], deepnees=deepnees+1)
                            new_value = check_status(dic2[key], dic1[key], deepnees=deepnees+1)
                else:
                    status = 'untouched'
                    old_value = dic1[key]
                    new_value = None
                value = {"status": status, "old_value": old_value, "new_value": new_value}
                dictionary[key]=value
    return dictionary

def n_convert(dict_inside, tab=' '):
    stroka = ''
    a = ''
    oper_plus = '+'
    oper_minus = '-'
    skobka2 = ''
    skobka1 = ''
    oper = ''
    inside = ''
    new_str='\n'
    dict_inside=dict_inside['children']
    print(dict_inside)
    for elem in list(dict_inside):
        for key in elem :
            a = a + key
            new_string = f'{new_str}{tab}{oper}{key}: {skobka1}{inside}{tab}{skobka2}\n'
            val = elem[key]
            if_dic = False
            if check_dic(val):
                if_dic = True
            if 'children' in val:
                skobka1 = '{'
                skobka2 = '}'
            status = val['status']
            if status == 'nested':
                #print('was nested')
                #print(key)
                inside = n_convert(val, tab=tab+tab)
                skobka1 = '{'
                skobka2 = '}'
            elif status == 'added' and check_dic(val):
                new_val = val['new_value']
                oper = oper_plus
                inside = new_val
            elif status == 'removed':
                oper = oper_minus
                old_val = val['old_value']
                inside = old_val
            elif status == 'changed':
                new_val = val['new_value']
                old_val = val['old_value']
                new_string = f'{tab}{oper_minus}{key}: {old_val}\n{tab}{oper_plus}: {key}{new_val}'
                #print('\n//////////////////////////////')
                #print(f'inside of changed : \n{tab}{inside}')
                #print('\n//////////////////////////////')
            #print(f'key : {key}')
            #print(f'val : {val}')
            stroka = stroka + new_string
    #print(f'-------------------------------\n{stroka}')
    return stroka


def low(element):
    if check_dic(element):
        #print(element)
        if 'status' in element:
            del element['status']
    if isinstance(element, bool):
        element = str(element).lower()
    elif isinstance(element, type(None)):
        element = 'null'
    return element


def check_dic(element):
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
    diff = check_status(file1,file2)
    #print('-------------------------------------------')
    #print(diff)
    #print('----------------------')
    #print('\n')
    #print(diff)
    #print('\n')
    fin_string = '{'
    diff_inside = diff['root']
    #print(type(diff_inside))
    n_convert(diff_inside)
    return fin_string


path1 = "file7.json"
path2 = "file8.json"
b = generate_diff(path1,path2)



#print('-------------------\n')
#print(b)
#print('\n-------------------')