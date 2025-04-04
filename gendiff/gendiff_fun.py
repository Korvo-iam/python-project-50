import json, yaml
from gendiff.codes_to_import.set_status import set_status
from gendiff.codes_to_import.plain_convert import plain_convert
from gendiff.codes_to_import.stylish_convert import stylish_convert


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


def generate_diff(first, second, format_name):
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
    if format_name == 'plain':
        fin_string = ''
        fin_string += plain_convert(diff_inside)
        fin_string = fin_string[:-1]
    else:
        fin_string = '{\n'
        fin_string += stylish_convert(diff_inside) + '}'
    return fin_string
