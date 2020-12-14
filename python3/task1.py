# Задача №1
#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division():
    try:
        number = input("Введите делимое число: ")
        divisor = input("Введите делитель : ")
        quotient = float(number)/float(divisor)
        print(f"Результат деления равен {quotient}")
    except ZeroDivisionError:
        print("На 0 делить нельзя!")
    except ValueError:
        print("Вы ввели не число!")

division()

