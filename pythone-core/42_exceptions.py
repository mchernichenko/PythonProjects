"""
1. Пространстра имён и область определения
   https://docs.python.org/3.7/reference/simple_stmts.html#the-global-statement
   * global - ключевое слово для определения глобальных переменных внутри функций

   https://docs.python.org/3.7/library/functions.html
   * locals()  - встроенная функция, возвращает словарь, содержащий имена локального пространства имен;
   * globals() - встроенная функция, возвращает словарь, содержащий имена глобального пространства имен.
   * _ и __ в именах переменных ЗАРЕЗЕРВИРОВАНЫ для использования внутри Python

2. try - except
"""

# 1. Использование глобальных переменных
global_var = 'value_global_var'


def print_global_var():
    """
    Это сторка документации:
    'Если не используется ключевое слово global внутри функции, Python задействует локальное пространство имен и переменная будет локальной'
    """
    global global_var  # для доступа на изменение глобальной переменной необходимо явно указать, что она глобальная, используя ключевое слово global
    print('Глобальная переменная: ', global_var)  # значение глобальной переменной можно получить внутри функции
    global_var = 'new_value'  # изменение глобальной переменной было бы невозможно, если бы не указали global global_var. Доступно было бы только чтение
    print('Новое значение глобальной переменной: ', global_var)

    lolal_var1 = 'value1'
    lolal_var2 = 'value2'
    print('Словарь локальных переменных: ', locals())
    print('В системной переменной __doc__ хранится строка её документации: ', print_global_var.__doc__)


print_global_var()

# имя функции находится в системной переменной __name__, а имя её строки документации в __doc__
print('Словарь глобальных переменных: ', globals())

# 2. try - exception


def division_int():
    """

    :return: функция возвращает частное от деления двух чисел
    """
    while True:
        value1 = input('Введите числитеть (q - выход): ')
        if value1 == 'q':
            break
        value2 = input('Введите знаменатель (q - выход): ')
        if value2 == 'q':
            break
        try:
            return int(value1) / int(value2)  # value1 = int(value1)

        # если ошибок не произошло, то исключение не обрабатываются, код просто пропускается
        except ValueError as err:  # присвоить переменной 'err' объект исключения, например, чтобы вывести stackTrace
            print('ERR: Требуется ввести числовые значения', err.__traceback__)
        except ZeroDivisionError:  # обект исколючения можно использовать напрямую
            print('ERR: Знаменатель не должен быть 0', ZeroDivisionError.__traceback__)
        except Exception as other:  # перехватывает все прочие ошибки. Важно его распологать последним (как в Java)
            print('ERR: Случилась неведомая хрень:', other.__traceback__)


print('\n == 2. Тестим try-exception ==')
print('Результат: ', division_int())
