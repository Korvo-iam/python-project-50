import json

import yaml

from gendiff.formatters.plain_convert import p_convert
from gendiff.formatters.stylish_convert import s_convert
from gendiff.scripts.set_diff_status import set_status


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


def generate(first, second, format_name='stylish'):
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
        fin_string = '' + p_convert(diff_inside)[:-1]
    elif format_name == 'stylish':
        fin_string = '{\n' + s_convert(diff_inside) + '}'
    elif format_name == 'json':
        fin_string = str(json.dumps(diff_inside, indent=4))
    return fin_string
