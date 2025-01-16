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

def kio(aro):
    for key, val in aro.items():
        print(key)
        print(val)
        print('------')

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



def check_status(dic1, dic2, list1):
    vortaro = {}
    for key in list1:
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
                    sortedlist = sorted(list(set(list(dic2[key].keys()) + list(dic2[key].keys()))))
                    old_value = check_status(dic1[key], dic2[key], sortedlist)
                    new_value = check_status(dic2[key], dic1[key], sortedlist)
        else:
            status = 'untouched'
            old_value = dic1[key]
            new_value = None
        value = {"status": status, "old_value": old_value, "new_value": new_value}
        vortaro[key]=value
    return vortaro


def low(element):
    if check_dic(element):
        print(element)
        if 'status' in element:
            del element['status']
    if isinstance(element, bool):
        element = str(element).lower()
    elif isinstance(element, type(None)):
        element = 'null'
    return element


def check_dic(element):
     if isinstance(element, dict):
         return True


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
    gen_list = sorted(list(set(list(file1.keys()) + list(file2.keys()))))
    #print(check_status(file1,file2,gen_list))
    #print(diff)
    diff = check_status(file1,file2,gen_list)
    #print('----------------------')
    #print(diff)
    #print(diff.items())
    for key,val in diff.items():
        print(key)
        print(val)
    
    #print(diff.keys())
    stroka = '{'
    stroka = stroka + convert_if_added(diff)
    stroka = stroka + convert_if_removed(diff)
    #print('stroka :')
    #print(stroka)
        #print(element)
        #print(diff[element])
    #print('---------------------------------------')
    #stroka_final = convert(diff)
    #return stroka_final
    return stroka


path1 = "file7.json"
path2 = "file8.json"
b = generate_diff(path1,path2)
print('-------------------\n')
print(b)
print('\n-------------------')