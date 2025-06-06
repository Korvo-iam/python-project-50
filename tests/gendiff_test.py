import json

from gendiff.scripts.generate_diff import generate

file1 = 'tests/test_data/file1.json'
file2 = 'tests/test_data/file2.json'
file3 = 'tests/test_data/file3.json'
file4 = 'tests/test_data/file4.json'
file5 = 'tests/test_data/file5.yaml'
file6 = 'tests/test_data/file6.yml'
file7 = 'tests/test_data/file7.json'
file8 = 'tests/test_data/file8.json'
file9 = 'tests/test_data/file9.yaml'
file10 = 'tests/test_data/file10.yaml'


def test_generate_diff_1():
    difference = generate(file1, file1)
    expected = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert difference == expected


def test_generate_diff_2():
    difference = generate(file1, file2)
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert difference == expected


def test_generate_diff_3():
    difference = generate(file1, file3)
    expected = '''{
  - follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert difference == expected


def test_generate_diff_4():
    difference = generate(file1, file4)
    expected = '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert difference == expected


def test_generate_diff_5():
    difference = generate(file3, file5)
    expected = '''{
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert difference == expected


def test_generate_diff_6():
    difference = generate(file1, file6)
    expected = '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert difference == expected


def test_generate_diff_7():
    difference = generate(file7, file8)
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    assert difference == expected


def test_generate_diff_8():
    difference = generate(file7, file8, 'plain')
    expected = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''
    assert difference == expected


def test_generate_diff_9():
    difference = generate(file7, file8, 'json')
    example_dic = {
    "status": "root",
    "children": [
        {
            "common": {
                "status": "nested",
                "children": [
                    {
                        "follow": {
                            "status": "added",
                            "old_value": None,
                            "new_value": False
                        },
                        "setting1": {
                            "status": "untouched",
                            "old_value": "Value 1",
                            "new_value": None
                        },
                        "setting2": {
                            "status": "removed",
                            "old_value": 200,
                            "new_value": None
                        },
                        "setting3": {
                            "status": "changed",
                            "old_value": True,
                            "new_value": None
                        },
                        "setting4": {
                            "status": "added",
                            "old_value": None,
                            "new_value": "blah blah"
                        },
                        "setting5": {
                            "status": "added_dic",
                            "children": [
                                {
                                    "key5": {
                                        "status": "untouched",
                                        "old_value": "value5",
                                        "new_value": None
                                    }
                                }
                            ]
                        },
                        "setting6": {
                            "status": "nested",
                            "children": [
                                {
                                    "doge": {
                                        "status": "nested",
                                        "children": [
                                            {
                                                "wow": {
                                                    "status": "changed",
                                                    "old_value": "",
                                                    "new_value": "so much"
                                                }
                                            }
                                        ]
                                    },
                                    "key": {
                                        "status": "untouched",
                                        "old_value": "value",
                                        "new_value": None
                                    },
                                    "ops": {
                                        "status": "added",
                                        "old_value": None,
                                        "new_value": "vops"
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "group1": {
                "status": "nested",
                "children": [
                    {
                        "baz": {
                            "status": "changed",
                            "old_value": "bas",
                            "new_value": "bars"
                        },
                        "foo": {
                            "status": "untouched",
                            "old_value": "bar",
                            "new_value": None
                        },
                        "nest": {
                            "status": "changed",
                            "old_value": {
                                "status": "untouched_dic",
                                "children": [
                                    {
                                        "key": {
                                            "status": "untouched",
                                            "old_value": "value",
                                            "new_value": None
                                        }
                                    }
                                ]
                            },
                            "new_value": "str"
                        }
                    }
                ]
            },
            "group2": {
                "status": "removed_dic",
                "children": [
                    {
                        "abc": {
                            "status": "untouched",
                            "old_value": 12345,
                            "new_value": None
                        },
                        "deep": {
                            "status": "nested",
                            "children": [
                                {
                                    "id": {
                                        "status": "untouched",
                                        "old_value": 45,
                                        "new_value": None
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "group3": {
                "status": "added_dic",
                "children": [
                    {
                        "deep": {
                            "status": "nested",
                            "children": [
                                {
                                    "id": {
                                        "status": "nested",
                                        "children": [
                                            {
                                                "number": {
                                                    "status": "untouched",
                                                    "old_value": 45,
                                                    "new_value": None
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "fee": {
                            "status": "untouched",
                            "old_value": 100500,
                            "new_value": None
                        }
                    }
                ]
            }
        }
    ]
}
    expected = str(json.dumps(example_dic, indent=4))
    assert difference == expected


def test_generate_diff_10():
    difference = generate(file9, file10)
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: too much
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
    group4: {
      - default: null
      + default: 
      - foo: 0
      + foo: null
      - isNested: false
      + isNested: none
      + key: false
        nest: {
          - bar: 
          + bar: 0
          - isNested: true
        }
      + someKey: true
      - type: bas
      + type: bar
    }
}'''
    assert difference == expected