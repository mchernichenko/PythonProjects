"""
  1) В Python все атрибуты public, но есть
  соглашение для скрытия атрибутов: имена следует начинать с двух нижних подчеркиваний (__)
  Но это не делает атрибут private, Python его переименовавыет в _<Имя_Класса>__<Имя_атрибута>

  Все методы класса должны иметь первым атрибутов - self, в который неавно передаётся экземпляр обекта (аналог this в java)

  2)  три вида методов: статические, класса и экземпляра класса
      Чаще всего метод класса используется тогда, когда нужен генерирующий метод, возвращающий объект класса или использующий статические атрибуты класса,
      например, счетчик экзеспляров класса.

      Статические методы в основном используются как вспомогательные функции и работают с данными, которые им передаются.
      Они не имеют доступа ни к самому классу, ни к его экземплярам.

  3) __init__ - конструктор
    __метод__ - специальные методы Python для сравнения объектов, выполнения каких-то вычислений и пр., например,
    реализация __eq__(self, other) позволит сравнивать обекты используя обычную операцию ==
    __add__() +
    __sub__() -
    __str__  вызывается при использовании print()
    __repr__ вызывается просто при выводе значения переменной ссылающейся на обект

    Про магические методы: https://docs.python.org/3.7/reference/datamodel.html?highlight=__add__#basic-customization
"""

class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property  # декоратор размещаемый перед геттером для атрибута __name
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter  # дероватор размещаемый перед сеттером для атрибута __name
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


inst_duck = Duck('old_value')
print('Получить атрибут "name": ', inst_duck.name)  # вызов геттера
inst_duck.name = 'new value'  # вызов сеттера
print('Получить атрибут "name": ', inst_duck.name)
# inst_duck.__name # а вот подучить доступ к __name нельзя, т.к. Python его изменяет
print('Прямой доступ к атрибуту: ', inst_duck._Duck__name)  #  прямой доступ к атрибуту, без геттера

# ===  3 вида методов: статические, класса и экземпляра класса

class ToyClass:
    def instancemethod(self):
        print('instance method called', self)
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        print('class method called', cls)
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        print('static method called')
        return 'static method called'


print('\n=== 2. виды методов ===')
obj = ToyClass()
obj.instancemethod()  # или можно так ToyClass.instancemethod(obj), что тоже самое
obj.classmethod()     # или можно так ToyClass.classmethod()
obj.staticmethod()    # или можно так ToyClass.classmethod()

# ==== пример использования =======
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod # этот метод со сути создаёт и возвращает экземпляр класса Person со своими атрибутами. В Java используется статический метод getInstance
    def getInstance(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod  # обычная вспомогательная функция, работающая только с данными, которые её передаются
    def is_adult(age):
        return age > 18

    # вызывается при использовании print(). Как переопределение toString в Java
    def __str__(self):
        return '__str__: name = ' + self.name + '; age = ' + str(self.age)

print('----------------------------')
person1 = Person('Sarah', 15) # классическое создание экземпляра
person2 = Person.getInstance('Roark', 1994)  # создание экземпляра через статический метод
print(person1)
print(person2)
print(Person.is_adult(15))

# ==========================
