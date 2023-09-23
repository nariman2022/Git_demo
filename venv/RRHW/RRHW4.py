#Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

# def square_cal(a):
#     p = 4*a
#     s = a*a
#     d = 2*a**2
#     print(f'Perimer is: {p}, Square is: {s}, Diagonal is: {d}')
#
# square_cal(6)

# Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# в формате аргумент: значение.

#def person(**kwargs):  # не работает
# def person(f_name='John', l_name='Small', age=35, position='QA', **status):
#     return f'Hello my name is {f_name} {l_name}. I am {age} years old. I work as a {position}.'
#
# print(person(f_name='Grace', l_name="Wild", position= 'DEVOPS'))

# Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
# положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# # new_list = [x for x in my_list if x > 0]
# # print(new_list)
#     return filter(lambda x: x for x in my_list if x > 0)

# Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

# Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# def decorator_fun(func):
#     def wrapper():
#         print(f'Wrapped function: {func.__name__}')
#         print(func())
#     return wrapper
#
# @decorator_fun
# def hello():
#     return 'I am wrapped function'

# Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.

# from my_calc import *
#
# print(deduct_it(5,3))
# print(sum_it (6,4))
# print(divide_it(9,3))
# print(multiply_it(5,6))


