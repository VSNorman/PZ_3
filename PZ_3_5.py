# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

import re

total = 0
ended = False

while not ended:
    numbers_str = input('Введите числа через проблем (для остановки программы напишите "стоп"): ')
    numbers = numbers_str.split(' ')

    numbers = map(lambda n: str(n).strip(), numbers)
    numbers = filter(lambda n: bool(n), numbers)

    shablon = r'^\d+$'

    for number in numbers:
        if number == 'стоп':
            ended = True
            break

        if not re.match(shablon, number):
            raise ValueError(f'Некорректное значение {number}.')

        total += int(number)

    print(f'Total result is: {total}')