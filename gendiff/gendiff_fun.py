import json
import yaml


from gendiff.codes_to_import.set_status import set_status
from gendiff.codes_to_import.plain_convert import plain_convert
from gendiff.codes_to_import.stylish_convert import stylish_convert
#from gendiff.codes_to_import.json_convert import json_convert


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


def generate_diff(first, second, format_name='stylish'):
    diff = {}
    if first is dict:
        file1 = first
    else:
        file1 = open_file(first)
    if second is dict:
        file2 = second
    else:
        file2 = open_file(second)
    diff = set_status(file1, file2)
    diff_inside = diff['root']
    fin_string = ''
    if format_name == 'plain':
        fin_string = ''
        fin_string += plain_convert(diff_inside)
        fin_string = fin_string[:-1]
    elif format_name == 'stylish':
        fin_string = '{\n'
        fin_string += stylish_convert(diff_inside) + '}'
    elif format_name == 'json':
        fin_string = str(json.dumps(diff_inside, indent=4))
        #print(fin_string)
    return fin_string

#a = 'files/file7.json'

#b = 'files/file8.json'
#generate_diff(a,b,'json')