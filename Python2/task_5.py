# Задача №5
# Первый вариант решения
a = []
print("Для окончания программы введите END!")
while True :
    b = input("Введите любое натуральное число : ")
    if b == 'END':
        print(a)
        break
    if b.isdigit():
        b = int(b)
        if b > 0:
            a.append(b)
            a.sort(reverse=True)
            print(a)
        if b == 0:
            print("0 не является натуральным числом!")
    else:
        if "-" in b:
            print("Вы ввели отрицательное число, оно не является натуральным!")
        elif "." in b:
            print("Вы ввели дробное число, оно не является натуральным!")
        else:
            print("Вы ввели не число, будьте внимательней!")

# Второй вариант решения, я попыталась поработать с Try/Except
a = []
print("Для окончания программы введите 0!")
print("(0 не является натуральным числом)")
while True:
    try:
        b = int(input("Введите любое натуральное число : "))
        if b == 0:
            print(a)
            break
        if b > 0:
            a.append(b)
            a.sort(reverse=True)
            print(a)
        elif b < 0:
            print("Вы ввели не натуральное число!")
    except ValueError:
        print("Вы ввели не натуральное число!")








