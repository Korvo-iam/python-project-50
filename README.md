### Hexlet tests and linter status:
[![Actions Status](https://github.com/Korvo-iam/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Korvo-iam/python-project-50/actions)

<a href="https://codeclimate.com/github/Korvo-iam/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/cff67099e9bb24915e6a/maintainability" /></a>

[![Test Coverage](https://api.codeclimate.com/v1/badges/cff67099e9bb24915e6a/test_coverage)](https://codeclimate.com/github/Korvo-iam/python-project-50/test_coverage)

ASCIINEMA:
[![asciicast](https://asciinema.org/a/cvDIJqch1bBuMT9xSZVb6XbJe.svg)](https://asciinema.org/a/cvDIJqch1bBuMT9xSZVb6XbJe)

## Links / Ссылки

🇷🇺
🇬🇧

Project on hexlet.io / Проект на hexlet.io : https://ru.hexlet.io/projects/50/members/41516/reviews

Github actions : https://github.com/Korvo-iam/python-project-50/actions

## Project description / Описание проекта

🇷🇺Generate_diff это проект который выводит разницу между двумя .json/.yaml/.yml файлами. Проект написан на Python версии 3.11 с использованием Makefile, uv и .toml-файла.

🇬🇧Generate_diff is a project that outputs the difference between 2 .json/.yaml/.yml files. Project is written in Python version 3.11 with usage of Makefile, uv and .toml-file.

У проекта есть три варианта вывода / The project has 3 options for output:
```bash
-f stylish
```
```bash
-f plain
```
```bash
-f json
```

## Installation / Установка

🇷🇺Используйте следующую команду чтобы построить проект

🇬🇧Run the following command to build the project

```bash
make build
```

🇷🇺Используйте следующую команду чтобы установить зависимые пакеты

🇬🇧Run the following command to install packages

```bash
make package-install / make package-install-venv
```

🇷🇺Далее установите uv с помощью указанной команды

🇬🇧Next install uv using command

```bash
make install
```

## Usage / Использование

```bash
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

```bash
Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

```bash
python3 -m gendiff.scripts.gendiff_script tests/test_data/file1.json tests/test_data/file2.json -f json
{
    "status": "root",
    "children": [
        {
            "follow": {
                "status": "removed",
                "old_value": false,
                "new_value": null
            },
            "host": {
                "status": "untouched",
                "old_value": "hexlet.io",
                "new_value": null
            },
            "proxy": {
                "status": "removed",
                "old_value": "123.234.53.22",
                "new_value": null
            },
            "timeout": {
                "status": "changed",
                "old_value": 50,
                "new_value": 20
            },
            "verbose": {
                "status": "added",
                "old_value": null,
                "new_value": true
            }
        }
    ]
}

```
