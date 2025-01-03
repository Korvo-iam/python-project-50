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
     if isinstance(element, dict):
         return True


def kto(val, stat):
    if isinstance(val,dict):
        #print(val)
        list_keys = list(val.keys())
        for key in list_keys:
            #print(f"-------{val[key]}")
            check_status(key, val,{})
            #print(f'status : {stat}')
            #print(f'valeu : {val}')
            if stat == 'removed':
                value_status = 'old_value'
            if stat == 'added':
                value_status = 'new_value'
            if stat == 'untouched':
                value_status = 'value'
    #print(f'status": {stat}, {value_status}: {val}')
    return {"status": stat, value_status: val}


def check_status(key, file1, file2):
    if key in file1 and key not in file2:
        status = "removed"
        if check_dic(file1[key]):
            file1[key] = kto(file1[key], status)
        valueold = file1[key]
        return {"status": status, "old_value": valueold}
    elif key not in file1 and key in file2:
        status = "added"
        if check_dic(file2[key]):
            file2[key] = kto(file2[key], status)
        valuenew = file2[key]
        return {"status": status, "new_value": valuenew}
    elif file1[key] != file2[key]:
        #print(key)
        #print(f'>>>>{file1[key]}')
        status = "changed"
        if check_dic(file1[key]):
            file1[key] = kto(file1[key], 'removed')
        if check_dic(file2[key]):
            file2[key] = kto(file2[key], 'added')
        valueold = file1[key]
        valuenew = file2[key]
        return {"status": status, "old_value": valueold, "new_value": valuenew}
    elif file1[key] == file2[key]:
        if check_dic(file1[key]):
            file1[key] = kto(file1[key], status)
        status = "untouched"
        valueold = file1[key]
        return {"status": status, "value": valueold}



def convert(element, step=" "):
    stroka = "{"
    #print(element)
    for key in element:
        if key == 'status':
            status = element[key]
        elif check_dic(element[key]) and 'status' in element[key]:
            status = element[key]['status']
        else:
            status = "untouched"

        if element[key] is not dict:
            result = element[key]
            #IF UNTOUCHED
        if status == "untouched":
            oper = " "
            stroka += f"\n{step} {oper} {key}: {low(result)}"
        elif status == "removed":
            #IF REMOVED
            if 'old_value' in element:
                if check_dic(element['old_value']):
                    value = convert(element['old_value'], step=step+step)
            elif 'old_value' in element[key]:
                if check_dic(element[key]['old_value']):
                     value = convert(element[key]['old_value'], step=step+step)
            else: value = low(element[key]['old_value'])
            oper = "-"
            stroka += f"\n{step} {oper} {key}: {value}"
            #IF ADDED
        elif status == "added":
            if 'new_value' in element:
                if check_dic(element['new_value']):
                    value = convert(element['new_value'], step=step+step)
            elif 'new_value' in element[key]:
                if check_dic(element[key]['new_value']):
                     value = convert(element[key]['new_value'], step=step+step)
            else: value = low(element[key]['new_value'])
            oper = "+"
            stroka += f"\n{step} {oper} {key}: {low(value)}"
            #IF CHANGED
        elif status == "changed":
            if 'old_value' in element:
                if check_dic(element['old_value']):
                    value = convert(element['old_value'], step=step+step)
            elif 'old_value' in element[key]:
                if check_dic(element[key]['old_value']):
                     value = convert(element[key]['old_value'], step=step+step)
            else: value = low(element[key]['old_value'])
            oper = "-"
            result = element[key]['old_value']
            stroka += f"\n{step} {oper} {key}: {low(result)}"
            if 'new_value' in element:
                if check_dic(element['new_value']):
                    value = convert(element['new_value'], step=step+step)
            elif 'new_value' in element[key]:
                if check_dic(element[key]['new_value']):
                     value = convert(element[key]['new_value'], step=step+step)
            else: value = low(element[key]['new_value'])
            oper = "+"
            result = element[key]['new_value']
            stroka += f"\n{step} {oper} {key}: {low(result)}"
    stroka += '\n'+ step + '}'
    return stroka


def generate_diff(first, second):
    diff = {}
    if first is not dict and second is not dict:
        file1 = open_file(first)
        file2 = open_file(second)
    else:
        file1 = first
        file2 = second
    gen_list = sorted(list(set(list(file1.keys()) + list(file2.keys()))))
    for el in gen_list:
        diff[el] = check_status(el, file1, file2)
    for element in diff:
        pass
        #print(element)
        #print(diff[element])
    #print('---------------------------------------')
    stroka_final = convert(diff)
    return stroka_final


path1 = "file7.json"
path2 = "file8.json"
b = generate_diff(path1,path2)
#print('-------------------\n')
print(b)
#print('\n-------------------')