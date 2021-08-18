# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

import re

def delenie(x, y):
    return x / y

if __name__ == '__main__':
    first_num = input('Введите первое число: ')
    second_num = input('Введите второе число: ')
    shablon = r'^\d+$'

    if not re.match(shablon, first_num) or not re.match(shablon, second_num):
        raise TypeError('Необходимо вводить только цифры')

    result = None

    try:
        result = delenie(int(first_num), int(second_num))
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
        exit(1)

    print(f'Result: {result}')