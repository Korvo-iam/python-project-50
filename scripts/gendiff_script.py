from gendiff import generate_diff
import json


file1 = json.load(open('../files/file1.json'))
file2 = json.load(open('../files/file2.json'))


__all__ = ('generate_diff')


