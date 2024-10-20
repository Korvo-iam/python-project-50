from gendiff.gendiff_fun import generate_diff


file1 = 'files/file1.json'
file2 = 'files/file2.json'
file3 = 'files/file3.json'
file4 = 'files/file4.json'


def test_generate_diff_1():
    difference = generate_diff(file1, file1)
    expected = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert difference == expected


def test_generate_diff_2():
    difference = generate_diff(file1, file2)
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
    difference = generate_diff(file1, file3)
    expected = '''{
  - follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert difference == expected


def test_generate_diff_4():
    difference = generate_diff(file1, file4)
    expected = '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert difference == expected