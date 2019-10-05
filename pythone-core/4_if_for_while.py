"""
https://docs.python.org/3.7/tutorial/controlflow.html#if-statements

Циклы
zip() - встроенная функция итерации по нескольким спискам. https://docs.python.org/3.7/library/functions.html#zip
range(start, stop[, step]) - встроенная функция генерации числовых последовательностей
Включения - компактный способ создать структуру данных:
    * Включение списков: [выражение for элемент in итерабельный объект if условие]
    * Включение словаря: { выражение_ключа: выражение_значения for выражение in итерабельный объект }
    * Включение множеств: {выражение for элемент in итерабельный объект if условие}
    * Включение кортежей: не существует

Что есть False:
    булева переменная False;
    значение None
    целое число 0;
    число с плавающей точкой 0.0;
    пустая строка (' ');
    пустой список ([]);
    пустой кортеж (());
    пустой словарь ({});
    пустое множество (set()).
"""

# условный оператор ################################################################################
color = 'red'
if color == 'blue':
    print('blue')
elif color == 'green':
    print('green')
else:
    print('bed color')

empty_list = list()  # пустое множество это False
if empty_list:
    print('не пустой список')
else:
    print('пустой список')

if 'M' in 'Misha':
    print('содержит "M"')

# Цикл While ################################################################################
numbers = [1, 2, 3, 4, 5]
pos = 0
while pos < len(numbers):
    elem = numbers[pos]
    if elem % 2 == 0:
        print(str(elem) + ' четное')
        break
    pos += 1
else:  # Проверка на прерывание цикла. В этот else заходим, если ниразу не случисля break или же его вообще нет
    print('чётных элеменов в списке нет')

# цикл for ################################################################################
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for keys, values in drinks.items():  # items() возвращает котреж (key, value), а по нему можно инициировать переменные
    print(keys, ' -> ', values)

list1 = [1, 2, 3, 4]
for elem in list1:
    if elem % 5 == 0:
        print(elem)
        break
else:  # аналогично while? выполняется, если были перебраны все элементы и цикл не прерывался
    print('Не дошли до конца списка')

#  функция zip() - итерация по нескольким спискам одинаковой длины. Иначе, итерация по самому короткому списку, остальное обрезается
list1 = [1, 2, 3]
list2 = [11, 22, 33]
list3 = [111, 222, 333, 444]
for a, b, c in zip(list1, list2, list3):
    print(a, ' ', b, ' ', c)

print(dict(zip(list1, list2)))  #  объединение листов в создание словаря

# функция range(start, stop[, step])
for x in range(2, -1, -1):
    print(x)

print(list(range(0, 11, 2)))

# Краткая форма создания структур данных
# Включение списков: [выражение for элемент in итерабельный объект if условие]
# Включение словаря: { выражение_ключа: выражение_значения for выражение in итерабельный объект }
# Включение множеств: {выражение for элемент in итерабельный объект if условие}
number_list = [number-1 for number in range(1, 6)]  #  [0, 1, 2, 3, 4]
number_list = [number for number in range(1,6) if number % 2 == 1]  # [1, 3, 5]

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]  # список кортежей

# включение словаря, т.е. гонерация словаря
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}  # {'t': 2, 'l': 1, 'e': 2, 'r': 1, 's': 1}

# включение множества
a_set = {number for number in range(1,6) if number % 3 == 1}

# включение кортежа нет, но ошибки не будет, т.к. возвращается обект-генератор, по которому можно итерироваться, но только один раз!
number_thing = (number for number in range(1, 6))
type(number_thing)  # <class 'generator'>
for number in number_thing:
    print(number)
