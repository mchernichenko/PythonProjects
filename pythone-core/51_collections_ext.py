"""
    Рассматриваются расширения из стандартной библтотеки Python для работы со структурами данных
    1) defaultdict - это по сути наследник класса dict, т.е. тот же самый словарь,
       НО в конструктор этого класса можно передать функцию, значением которой будут инициироваться отсутствующие значения
    2) OrderedDict - это словарь в котором запоминается порядок добавления в него ключей
    3) Counter - класс, позволяющий собирать статистику по спискам
    4) deque - двунаправленная очередь
    5) Особые итераторы
       itertools содержит особые функции итератора. Каждая из них возвращает один элемент при каждом вызове из цикла for … in и запоминает свое состояние между вызовами.
    6) именованные кортежи - это подкласс класса Turple, с помощью которых можно получить доступ к значениям по имени
       По сути это неизменяемый объект, у которого атрибуты и есть элементы котрежа, а именованного потому, что атрибут же имеет имя и значение
       но кортежи более эффективны, чем обычный объект с точки зрения времени и занимаемого места

"""

# РАСШИРЕНИЯ словарей

# ===== 1. defaultdict ===========================================
from collections import defaultdict

dict1 = defaultdict(int)  # Аргументом defaultdict() является функция. Теперь любое отсутствующее значение будет заменяться целым числом (int) 0:
dict1['key1'] = 1
a = dict1['key2']  # здесь ключу присваивается дефалтовое значение и возвращается значение, как будто оно есть в словаре
print('defaultdict: ', list(dict1.items()))

def no_idea():
    return 'default value'

dict1 = defaultdict(no_idea)
dict1['key1'] = 'value1'
a = dict1['key2']
print('defaultdict: ', list(dict1.items()))

# === 2. OrderedDict ===============================================
from collections import OrderedDict

quotes = OrderedDict([('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')])
for stooge in quotes:
    print(stooge)  # гарантированно выдет ключи в порядке: key3, key2, key1

# == 3. Counter ===================================================
from collections import Counter

list1 = ['spam', 'spam', 'eggs', 'spam']
list2 = ['eggs', 'eggs', 'bacon']

list1_counter = Counter(list1)
list2_counter = Counter(list2)

print(list1_counter.most_common())  # [('spam', 3), ('eggs', 1)] - возвращает количество вхожлений каждого элемента списка
print('Разность счётчиков: ', list1_counter - list2_counter)  # Над счетчиками можно выполнять операции как над множествами
print('Сумма счётчиков: ', list1_counter + list2_counter)
print('Пересечение счётчиков: ', list1_counter & list2_counter)  # В результате пересечения был получен общий элемент ('eggs') с низким значением счетчика

# == 4. deque ==================================================
from collections import deque

def palindrome(word):
    """
    Функция определения палиндрома с помощью двунаправленной очереди
    :param word:
    :return: True, если указанное слово является палиндромом
    """
    dq = deque(word)  # создаём очередь
    while len(dq) > 1:
        if dq.popleft() != dq.pop():  # Функция popleft() удаляет крайний слева элемент deque и возвращает его, функция pop() удаляет крайний справа элемент и возвращает его.
            return False
        return True

print('Это палиндром? ', palindrome('racecar'))

# == 5. itertools ===========================================
import itertools

for item in itertools.chain([1, 2], ['a', 'b']):  # сквозное итерирование
    print('chain:', item) # 1, 2, a, b

for item in itertools.accumulate([1, 2, 3, 4]):  # итерация с подсчтом накопленных значений
    print('accumulate', item)  # 1,3,6,10

# == pprint ==============================
from pprint import pprint

# == 6. именованные кортежи
from collections import namedtuple

print('\n== именованные кортежи')
# Говорим, создай подкласс Point класса Tuple, который будет хранить 2 атрибута с именами 'x' и 'y'
# Именованные кортежи удобно использовать вместо обычных неизменяемых обектов, т.к. они более эффектифны
Point = namedtuple('Point', 'x y')  # возвращается подкласс Point класса Tuple. Можно и так namedtuple('Point', ['x, y'])
                                    # т.к. внутри используется 'x y'.split()

pt1 = Point(x=1.0, y=5.0)  # создаём кортеж из двух элементов, т.е. по сути создаём экземпляр объекта с определёнными значениями атрибутов
pt2 = Point(2.5, 1.5)

point3 = {'x': 1, 'y': 2}
pt3 = Point(**point3)  # именованный кортеж можно создать из словаря
pt4 = pt3._replace(x=77)  # создать на базе существующего новый кортеж

print(pt1.x, pt1.y)
print(pt3.x, pt3.y)
print(pt4.x, pt4.y)

