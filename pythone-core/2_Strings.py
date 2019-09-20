"""
Про строки https://docs.python.org/3.7/tutorial/introduction.html#strings
1. Объявление строк
2. Преобразование в строку str(), использование управляющих символов \n, \t, объединение
3. Извлечение символов

"""

# 1. Объявление строк

str1 = 'Строка, внутри которой м.б. двойные кавыйчи'
str1 = "Это тоже 'строка', внутри которой м.б. одинарные кавычки"

long_str = """ Оччееееееееень 
длиннааааааааааа
строка"""
print(long_str)

# 2. Преобразование в строку str(), использование управляющих символов \n, \t, объединение
print(str(98.99))
print(str(True))
print('aaaaaa\nbbbbbbbbbb')  # вывод в 2 строки
print(3 * 'a' + 4 * 'b')  # aaabbbb

# 3. Извлечение символов. Стока - это по сути котреж символов => со сторокой можно работать как массивом символов
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0]+letters[-1])  # 'ax' печать первого и последнего символа
# letters[100] смещение не должно аревышать длину строки
# letters[1] = 'Q' строки не изменяемы!!!

# Использование срезов или вычленение подстрок: letters[start:stop:step], т.е. [start, stop)
print(letters[2:-1:2])  # 'cegikmoqsuwy' посдтрока начиная с 3-го символа, до предпоследнего c шагом 1 до через один
print(letters[:-4:-1])  # 'zyx' шагаем с конца до 4-го символа с конца (сам он не включается)

print(letters[24:100:])  # 'yz' !! в срезах можно выходить за границы длины строки. Т.к. 100 превышает длину, то берётся -1
print(letters[-100:2:])  # 'ab' !! т.к. -100 превышает длину по модуюлю, то бер1тся 0

# 4. Разные функции со строками: len(), split(), string.join(list)
letters = 'abcdefghijklmnopqrstuv0wxyz'
print('Длина ' + str(len(letters)))

print('aaa,bbb,ccc,ddd,eee'.split(','))  # ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print('aaa bbb   ccc ddd\teee'.split())  # ['aaa', 'bbb', 'ccc', 'ddd', 'eee'] т.к. по умолчанию в качестве разденителя используется пробел \n, \t

print('\t'.join(['aaa', 'bbbb']))  # aaa	bbbb

print(letters.upper()[:3])  # ABC
letters.startswith('abc')  # True
print('  aaa   '.strip())  # удаление пробелов с обоих концов строки
print('123456789'.replace('234','xxx'))  # 1xxx56789
