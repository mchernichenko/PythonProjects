"""
https://docs.python.org/3.7/tutorial/controlflow.html#if-statements

Циклы и встроенная функция zip() https://docs.python.org/3.7/library/functions.html#zip

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

for keys, values in drinks.items(): # items() возвращает котреж (key, value), а им можно инициировать переменные
    print(keys, ' -> ', values)

list = [1, 2, 3, 4]
for elem in list:
    if elem % 5 == 0:
        print(elem)
        break
else:  # аналогично while? выполняется, если были перебраны все элементы и цикл не прерывался
    print('Не дошли до конца списка')

# итерация по нескольким спискам одинаковой длины - функция zip(). Иначе, итерация по самому короткому списку, остальное обрезается
list1 = [1, 2, 3]
list2 = [11, 22, 33]
list3 = [111, 222, 333, 444]
for a, b, c in zip(list1, list2, list3):
    print(a, ' ', b, ' ', c)

print(dict(zip(list1, list2))) #  объединение листов в создание словаря
