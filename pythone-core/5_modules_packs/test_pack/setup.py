"""
    Файл описания дистрибутива. Он должен запустаться с ключом 'sdist', чтобы создать zip-архив с исходниками, например,
    > python setup.py sdist  bdist_wheel
    Справка по команде: python setup.py --help-commands
"""
from setuptools import setup, find_packages

setup(name='test_pack_name',  # определяет имя дистрибутива
      version='1.0',
      description='Description pack',
      author='mchernichenko',
      author_email='mchernichenko@mail.ru',
      url='mchernichenko.ru',
      py_modules=['daily', 'weekly'],  # список файлов .py, которые нужно включить в пакет
   #   packages=find_packages()
      )