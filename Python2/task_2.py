# Задача №2
# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
m = int(input("Скользо значений вы хотите добавить в список: "))
a =[]
i = 0
while i < m:
    a.append(input("Введите значение: "))
    i+=1
for el in range(1,len(a),2):
    a[el-1], a[el] = a[el], a[el-1]
print(a)


b = input("Введите значения через пробел: ").split()
for el in range(1,len(b),2):
    b[el-1], b[el] = b[el], b[el-1]
print(b)

