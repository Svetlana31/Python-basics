# Задача №3
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# Первый вариант решения
def my_func(a, b, c):
    try:
        spisok = [a, b, c]
        spisok.remove(min(spisok))
        print(sum(spisok))
    except TypeError:
        print("Разные типы данных!")
my_func(5, 2, 4)



# Второй вариант решения
def my_func(a, b, c):
    try:
        spisok = [a, b, c]
        spisok.sort()
        result = spisok[1] + spisok[2]
        print(result)
    except TypeError:
        print("Разные типы данных!")
my_func(6, 3.2, 3)





