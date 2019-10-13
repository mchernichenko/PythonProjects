"""
1. Существует два способа чтения файлов CSV. Использовать функцию чтения модуля csv, или использовать класс DictReader
    https://python-scripts.com/import-csv-python

"""

import csv
from collections import OrderedDict

villains = [#['first_name', 'last_name'],
            ['Doctor', 'No'],
            ['Rosa', 'Klebb'],
            ['Mister', 'Big'],
            ['Auric', 'Goldfinger'],
            ['Ernst', 'Blofeld']
           ]

# запись в файл
with open('test_csv', 'wt', newline='') as fout:  # менеджер контекста.
                                # поскольку модуль csv выполняет собственную обработку новой строки, вставляющий \r,нужно указать newline="
    csvout = csv.writer(fout, delimiter=',')  # получить объект записи в файл
    csvout.writerows(villains)

# чтение из файла
with open('test_csv', 'rt') as fin:  # менеджер контекста
    reader = csv.reader(fin)
    villains = [row for row in reader] # Здесь используется включение списка

print(villains)

# данные могут иметь формат списка словарей, а не списка списков
# Чтение файлов CSV
with open('test_csv', 'rt') as fin:
    reader = csv.DictReader(fin, delimiter=',', fieldnames=['first_name', 'last_name'])  # указываем имена колонок, если файл не имеет строки с заголовками
    for line in reader:
        print(line['first_name'], line['last_name'])
    # villains = [row for row in reader]

# Пишем CSV файл
villains = [
{'first': 'Doctor', 'last': 'No'},
{'first': 'Rosa', 'last': 'Klebb'},
{'first': 'Mister', 'last': 'Big'},
{'first': 'Auric', 'last': 'Goldfinger'},
{'first': 'Ernst', 'last': 'Blofeld'},
]

with open('test_csv', 'wt',  newline='') as fout:
    writer = csv.DictWriter(fout, ['first', 'last'])
    writer.writeheader()
    writer.writerows(villains)

with open('test_csv', 'rt') as fin:
    reader = csv.DictReader(fin)
    villains = [row for row in reader]

print(villains)