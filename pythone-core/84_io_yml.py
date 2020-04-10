"""
Общий обзор YAML, сравнение с JSON и примеры работы в Python
https://rtfm.co.ua/what-is-yaml-obshhij-obzor-tipy-dannyx-yaml-vs-json-i-pyyaml/

"""

import yaml


with open('test_yaml.yml', 'rt') as fin:
    text = fin.read()

data = yaml.load(text, Loader=yaml.FullLoader)
# data = yaml.load (open('test_yaml.yml', 'rt'), Loader=yaml.FullLoader) # можно сразу считать  yaml
print('yaml_data: ', data)

