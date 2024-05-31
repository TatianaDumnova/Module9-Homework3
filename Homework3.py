# Домашнее задание по теме "Итераторы"
# Цель работы
# Применить dunder методы iter, next в своём классе
# Задание
# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.
# При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)
# Примечание
# Значение атрибута start всегда меньше значения атрибута end
# В решении задачи не использовать list, tuple и др. встроенные типы данных.
# Входные данные
# en = EvenNumbers(10, 25)
# for i in en:
# print(i)
# Выходные данные
# После перебора и вывода:
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24

class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = self.start - 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.start:
            if self.i > self.end:
                raise StopIteration()
            self.start = self.start + 1
        return self.start


en = EvenNumbers(10, 25)
for i in en:
    if i % 2 == 0:
        print(i)

