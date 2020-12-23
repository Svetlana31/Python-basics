# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
with open(file="task4_less5.txt", encoding="UTF-8", mode="rt") as file:
    lst = []
    a = []
    rus = ["Один", "Два", "Три", "Четыре"]
    for line in file:
        lst.append(line.split())
    i = 0
    while i < len(lst):
        lst[i][0] = rus[i]
        i += 1
    for el in lst:
        a.append(' '.join(el))
file = open(file='task4_2_l5.txt', encoding='UTF-8', mode='wt')
file.writelines('\n'.join(a))
file.close()


