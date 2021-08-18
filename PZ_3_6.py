# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def big_letter(string):

    words = str(string).split(' ')

    words = filter(lambda w: bool(w), words)
    words = map(lambda w: str(w[0]).upper() + str(w[1::]), words)

    return ' '.join(words)


if __name__ == '__main__':
    input_word = input('Введите слова с маленькой буквы через пробел: ')
    itog = big_letter(input_word)

    print(f'Result: {itog}')