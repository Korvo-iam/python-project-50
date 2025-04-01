import json
import yaml
from codes_to_import import set_status, plain_convert, stylish_convert


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
    diff = set_status.set_status(file1, file2)
    diff_inside = diff['root']
    if format_name == 'stylish':
        fin_string = '{\n'
        fin_string += stylish_convert.stylish_convert(diff_inside) + '}'
    elif format_name == 'plain':
        fin_string = ''
        fin_string += plain_convert.plain_convert(diff_inside)
        fin_string = fin_string[:-1]
    return fin_string

a='files/file1.json'
b='files/file2.json'
c = generate_diff(a,b)
print(c)