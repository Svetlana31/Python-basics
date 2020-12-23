# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open(file="task_5_less5", encoding="UTF-8", mode="wt") as file:
    lst = input("Введите числа через пробел: ").split()
    file.writelines(' '.join(lst))
    numbers = [int(el) for el in lst]
    print(f"Сумма чисел в файле равна {sum(numbers)}")

