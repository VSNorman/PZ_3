# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    numbers = (x, y, z)
    numbers = sorted(numbers, reverse=True)

    return numbers[0] + numbers[1]


if __name__ == '__main__':
    result = my_func(15, 18, 10)

    print(f'Result: {result}')
