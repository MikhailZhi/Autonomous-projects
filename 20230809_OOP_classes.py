# Эволюция: потоковое (из строк) программирование, процедурное (из функций) программирование,
# Объектно Ориентированное Программирование (ООП)
# Объект - сущность, объединяющая данные и методы для работы с ними (состояние и поведение)
# Аналогии: чертеж - класс, а дом - объект. Класс - новый тип данных, а объект - его представитель
# У любого объекта есть: id, значение, type
# Классы нужны: Первое, когда не хватает встроенных типов данных. Второе, когда надо несколько состояний.
# Метод - это функция, которая принадлежит классу
# dunder (=double under) - магические методы (с двумя подчеркиваниями)

class Cat:
    def __init__(self, name, age):  # (магический метод) при создании объекта, что нужно указывать
        self.name = name
        self.age = age

    def meow(self):  # метод для мяу котом
        print(f'{self.name} says: Meow')
        print(f'Self of {self.name} :{self}')


tom = Cat('Tom', 2)
angela = Cat('Angela', 3)


def first_steps():
    print(f'\nIs tom == angels: {tom is angela}')
    print(f'address of tom object: {tom}')  # address of tom object
    print(f'address of angela object: {angela}')  # address of angela object
    print(f'type of tom: {type(tom)}\n')


def object_methods():
    tom.meow()
    Cat.meow(angela)  # equal angela.meow()
    print(f'tom.name = {tom.name}')
    print(f'tom.age = {tom.age}')


if __name__ == '__main__':
    first_steps()
    object_methods()
