"""
  Модули - Пакеты - Дистрибуция модулей

1. МОДУЛЬ в Python - просто файл с расширением .py, в котором хранятся функции

  Существует два способа импорта модулей
  * import module as alias -- импорт всего пакета, которому можно назначить алиас
  * from module import func as alias - импорт конкретной функции, которой можно назначить алиас
  Как правило вси импорты пишутся вначале файла, но можно делать импорт непосредственной в функции, но это не прозоачно

  Python при  импорте производит поиск (sys.path)
  * сначала в текущем каталоге,
  * затем в хранилище сторонних пакетов (<USER>\AppData\Local\Programs\Python\Python37\Lib\lib\site-packages в Windows или  /usr/lib/pythonX.X/site-packages на Linux)
  * затем каталогах стандартной библиотеки
  при ниличии одинаковых имён модулей, будет использоваться первый найденный

2. ПАКЕТы используются для формирования пространства имен, что позволяет работать с модулями через указание уровня вложенности (через точку).
   Пакет а Python - это каталог, включающий в себя другие каталоги и модули и дополнительно содержащий файл __init__.py
   Чтобы считать папку пакетом, в ней д.б. файл __init__.py

   __init__.py м.б. пустым или хранить список модулей в переменной __all__, которые импортируются командой from <имя_модуля> import *, например:
   __all__ = ['file1, 'file2', 'file3']

   Пакеты позволяют работать с модулями через указание уровня вложенности (через точку): 
   import <имя пакета>
   <имя_пакета>.<имя_файла>.<имя_функции>

3.  ДИСТРИБУЦИЯ модулей: https://docs.python.org/3.7/distributing/index.html?highlight=setuptools
    Добавление модуля в хранилище сторонних пакетов с помощью встроенной тулзы setuptools: python -m pip install --user --upgrade setuptools wheel
    https://setuptools.readthedocs.io/en/latest/

    1) Создать описание дистрибутива в файле setup.py
    2) Сгенерировать файл дистрибутива в папке 'dist'. На этом этапе в папке должны быть min три файла: <сам модуль>.py, setup.py и README.txt.
       > python setup.py sdist bdist_wheel
       Остальные команды можно просмотреть так: python setup.py --help-commands
    3) Установить файл дистрибутива - (фактически копирует сюда /lib/site-packages)
       > pip install <имя_модуля>.tar.gz

    <TBD> - разобраться с дистрибуцией пакетов

"""

# 1. импорт
import sys
import test_module  # импорт всех функций пользовательского модуля
from test_module import test_func  # импорт определённой функции модуля

for p in sys.path:
    print(p)  # в этих каталогах ищутся модули

print(test_module.test_func())
print(test_func())  # если импортировать функциюю, то её можно вызывать без указания имени модуля

# 2. Пакеты
from test_pack import daily, weekly  # из пакета импортируются определённые модули

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

import daily
print("!! Daily forecast:", daily.forecast())




