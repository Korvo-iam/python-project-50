from gendiff.gendiff_fun import generate_diff


def test_generate_diff():
    difference = generate_diff(file1.json, file1.json)
    expected = '''{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
    }'''
    assert difference == expected
    difference = generate_diff(file1.json, file2.json)
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
    }'''
    assert difference == expected
    difference = generate_diff(file1.json, file3.json)
    expected = '''{
  - follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
    }'''
    assert difference == expected
    difference = generate_diff(file1.json, file4.json)
    expected = '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
    }'''
    assert difference == expected