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


def low(element):
    if isinstance(element, bool):
        element = str(element).lower()
    elif isinstance(element, type(None)):
        element = 'null'
    return element


def dua(key, file1, file2):
    if key in file1 and key not in file2:
        status = "removed"
        valueold = file1[key]
        return{"status":status, "old_value":valueold}
    elif key not in file1 and key in file2:
        status = "added"
        valuenew = file2[key]
        return{"status":status, "new_value":valuenew}
    elif file1[key] != file2[key]:
        status = "changed"
        valueold = file1[key]
        valuenew = file2[key]
        return{"status":status, "old_value":valueold, "new_value":valuenew}
    elif file1[key] == file2[key]:
        status = "untouched"
        valueold = file1[key]
        return{"status":status, "value":valueold}


def convert(element, step = " "):
    stroka = "{"
    for el in element:
        #print(el)
        if element[el]['status'] == "untouched":
            oper = " "
            stroka += f"\n{step} {oper} {el}: {low(element[el]['value'])}"
        elif element[el]['status'] == "removed":
            oper = "-"
            stroka += f"\n{step} {oper} {el}: {low(element[el]['old_value'])}"
        elif element[el]['status'] == "added":
            oper = "+"
            stroka += f"\n{step} {oper} {el}: {low(element[el]['new_value'])}"
        elif element[el]['status'] == "changed":
            oper = "-"
            stroka += f"\n{step} {oper} {el}: {low(element[el]['old_value'])}"
            oper = "+"
            stroka += f"\n{step} {oper} {el}: {low(element[el]['new_value'])}"
    stroka += "\n}"
    return stroka

def generate_diff(first, second):
    diff = {}
    file1 = open_file(first)
    file2 = open_file(second)
    gen_list = sorted(list(set(list(file1.keys()) + list(file2.keys()))))
    for el in gen_list:
        diff[el] = dua(el,file1,file2)
    stroka_final = convert(diff)
    return stroka_final