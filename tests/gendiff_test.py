from gendiff import gendiff_fun

file1 = 'files/file1.json'
file2 = 'files/file2.json'
file3 = 'files/file3.json'
file4 = 'files/file4.json'
file5 = 'files/file5.yaml'
file6 = 'files/file6.yml'
file7 = 'files/file7.json'
file8 = 'files/file8.json'


def test_generate_diff_1():
    difference = gendiff_fun.generate_diff(file1, file1)
    expected = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert difference == expected


def test_generate_diff_2():
    difference = gendiff_fun.generate_diff(file1, file2)
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
    difference = gendiff_fun.generate_diff(file1, file3)
    expected = '''{
  - follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert difference == expected


def test_generate_diff_4():
    difference = gendiff_fun.generate_diff(file1, file4)
    expected = '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert difference == expected


def test_generate_diff_5():
    difference = gendiff_fun.generate_diff(file3, file5)
    expected = '''{
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert difference == expected


def test_generate_diff_6():
    difference = gendiff_fun.generate_diff(file1, file6)
    expected = '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert difference == expected


def test_generate_diff_7():
    difference = gendiff_fun.generate_diff(file7, file8)
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
    difference = gendiff_fun.generate_diff(file7, file8, 'plain')
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
