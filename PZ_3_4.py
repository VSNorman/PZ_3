# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

import re

def expon(number_one, number_two):
    if number_two < 1:
        raise ValueError(f'Показтель степени не может быть меньше единицы')
    result = number_one
    for _ in range(1, number_two):
        result = result * number_one
    return result

if __name__ == '__main__':
    number_one = input('Введите первое число: ')
    number_two = input('Введите второе число: ')
    shablon = r'^\d+$'

    if not re.match(shablon, number_one) or not re.match(shablon, number_two):
        raise TypeError('Необходимо вводить только цифры')
    result = expon(int(number_one), int(number_two))

    print(f'Result: {result}')

