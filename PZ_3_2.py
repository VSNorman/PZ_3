# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def list (name, surname, birthday, city, email, tel):
    print(f'{name} {surname} родился {birthday} году, живет в городе {city}. Контакты: {email}, {tel}')


list(name='Павел', surname='Васин', birthday='1856', city='Мурманск', email='VP_PV@mail.com', tel='+98954851838')