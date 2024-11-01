from gendiff import gendiff_fun


file1 = 'files/file1.json'
file2 = 'files/file2.json'
file3 = 'files/file3.json'
file4 = 'files/file4.json'
file5 = 'files/file5.yaml'
file6 = 'files/file6.yml'


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
