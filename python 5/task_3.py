# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open(file="task3_less5.txt", encoding="UTF-8", mode="rt") as file:
    lst = [line.split() for line in file]
    people = [el[0] for el in lst if int(el[1]) < 20000]
    numbers = [int(el[1]) for el in lst]
print(f"Оклад менее 20тыс. имеют: {', '.join(people)}.")
print(f"Средняя величина дохода сотрудников составляет: {sum(numbers)/len(numbers)}")








