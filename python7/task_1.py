#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
#который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д
class Matrix():
    def __init__(self, lst_1, lst_2):
        self.lst_1 = lst_1
        self.lst_2 = lst_2
        self.lst = [lst_1, lst_2]

    def __str__(self):
        spisok = []
        s = 0
        while s < len(self.lst):
            for el in self.lst[s]:
                spisok.append(str(el))
            s += 1
        return ' '.join(spisok)

    def __add__(self, other):
        numbers = []
        rez = []
        n = 0
        while n < len(self.lst):
            for i in range(len(self.lst)):
                for j in range(len(self.lst[n])):
                    sum = self.lst[n][j] + other.lst[n][j]
                    numbers.append(sum)
                if len(numbers) == len(self.lst[n]):
                    rez.append(numbers)
                    numbers = []
                n += 1
        return rez



a = Matrix([1, 2, 3], [4, 5, 6])
b = Matrix([7, 8, 9], [10, 11, 12])
print(a.lst)
print(a)
print(a + b)

