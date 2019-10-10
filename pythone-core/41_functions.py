"""
  1. Аргументы по умолчанию, должны определяться последними
  2. Позиционые аргументы и Аргументы - ключевые слова, т.е. от позиции не зависит, т.к. указывается имя агрумента и его значение при вызове, по аналогии с PL/SQL
  3. Комментари к функции и передача произвольного количества аргументов
     *args - кортеж аргументов
     **kwargs - словарь аргументов
  4. Заглушки - pass
  5. Функция - это тоже объект, который можно передавать как аргумент
  6. Внутренние функции
  7. Замыкания - функция, которая динамически генерируется другой функциией
  8. Анонимная, lambda() функция - функция без имени, по сути разово используемаяк
  9. Генераторы - обычная функция, но она возвращает значение с помощью выражения yield, а не return.
     При вызове yield не прекращает работу, а 'замораживается' до следующей итерации, запускаемой функцией next()
     Пример штатного генератора - функция range()
  10. Дакораторы -- это функция, которая принимает одну функцию в качестве аргумента и возвращает другую функцию

  None - это специальное значение в Python, которое заполняет собой пустое место.
  None потребуется вам, чтобы отличить отсутствующее значение от пустого. Пустые структкры равны False, но не равны None
   Оно не является булевым значением False.
"""


# 1. аргументы по умолчанию, должны перечисляться последними
def menu(arg1, arg2='def_val2', arg3='def_val3', result=None):
    if result is None:  # проверка первого вызова функции
        result = []
    result.append(arg1)
    result.append(arg2)
    result.append(arg3)
    return result


print('default values: ', menu('1', 'w'))

# Важно: значения по-умолчанию вычисляются и ассоциируются только один раз – в момент объявления функции
def_val = 2


def our_func(val=def_val):
    print(val)


our_func(4)  # выведет 4
our_func()  # выведет 2 – значение по-умолчанию
def_val = 12
our_func()  # все равно 2, так как def_val было равно 2 на момент объявления

# 2. Позиционные аргументы и аргументы - ключевые слова
print(menu('beef',
           'bordeaux'))  # ['beef', 'bordeaux', 'default value']  - значения аргументов определяются в зависимости от позиции
print(menu(arg2='beef',
           arg1='bordeaux'))  # ['bordeaux', 'beef', 'default value'] - - значения аргументов определяются по имени


# 3. передача неограниченного количестовоа позиционных или непозиционных аргументов
#    Комментарии к функциям
def print_args(*args, **kwargs):
    """
    Функция печати переданных аргументов
    :param args: кортеж параметров
    :param kwargs: словарь параметров
    :return: ничего не возвращает
    """

    print('Positional argument tuple:', args)
    print('Keyword arguments:', list(kwargs.items()))


print_args(3, 2, 1, 'qqq', arg1='www', arg2=4)  # передача произвольеого количества параметров в функцию
help(print_args)  # вывод справки по функции


# 4. Заглушка
def do_nothing():
    pass  #


# 5. Передача функции как аргумента
def run_something_with_args(func, arg1, arg2):
    return func(arg1, arg2)


print('\n== 5. Передача функции как аргумента ==')
print(run_something_with_args(menu, 'arg1', 'arg2'))


# 6. Внутренние функции
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote

    return inner(saying)


# 7. Замыкание
def knights2(saying):
    """
    Функция возвращающая внутренню функцию
    :param saying:
    :return: Возвращает внутреннюю функцию
    """

    def inner2():
        return "Значение внешнего параметра: '%s'" % saying

    return inner2


print('\n== 7. Замыкания ==')
a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(a())  # Это вызов разных функций
print(b())


# 8. Анонимная, lambda() функция - функция без имени, по сути разово используемаяк
def edit_story(words, func):
    for word in words:
        print(func(word))


print('\n== 8. Use lambda ==')
# Лямбда принимает один аргумент, который в этом примере назван word. /
# Все, что находится между двоеточием и закрывающей скобкой, является определением функции.
edit_story(['thud', 'meow', 'thud', 'hiss'], lambda word: word.capitalize() + '!')


# 9. Генераторы - обычная функция, но она возвращает значение с помощью выражения yield, а не return.
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number  # При вызове yield не прекращает работу, а 'замораживается' до следующей итерации, запускаемой функцией next()
        number += step


print('\n== 9. Генераторы ==')
my_rng = my_range()
print('my_rng, текущая позиция итератора', next(my_rng))
print('my_rng, текущая позиция итератора', next(my_rng))
print('my_rng, текущая позиция итератора', next(my_rng))

# проитерировать можно через конструкцию for
for x in my_range(1, 4, ):  # for по сути вызывает next()
    print('my_range', x)


#  10. Декораторы - это функция, которая принимает одну функцию в качестве аргумента и возвращает другую функцию
def func_decorator(func):
    def new_function1(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result func_decorator:', result)
        return result
    return new_function1

def square_it(func):  #  ещё один декоратор
    def new_function2(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Result square_it:', result * result)
        return result * result

    return new_function2


# Декорируемая функция
def add_ints_1(a, b):
    return a + b

#
@func_decorator  # данная конструкция нужна для автоматической обёртки функции
@square_it       # данный декоратор выполнится первым
def add_ints_2(a, b):
    return a + b

print('\n== 10. Декораторы ==')
print('\n- Ручной вызов обёртки -')
decor = func_decorator(add_ints_1)  # ручное создание обёртки к add_ints. В этом случае конструкция @func_decorator не требуется
decor(3, 5)

print('\n- Автоматический вызов обёртки -')
add_ints_2(3, 5)


#
print('\n')
def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")


is_none(None)  # It's None
is_none([])  # It's False
