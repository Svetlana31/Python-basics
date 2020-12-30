class Cell():
    def __init__(self,number):
        self.number = int(number)
    def __add__(self, other):
        return Cell(self.number + other.number)
    def __str__(self):
        return f"Колличество ячеек клетки: {self.number} {self.number * '*' }"

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            return "Разность меньше нуля!"

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number / other.number))

    def make_order(self, row):
        self.row = row
        if self.number % self.row != 0:
            r = ""
            for i in range(self.number // self.row):
                r += f'{"*" * self.row }\\n'
            r += f'{"*" * (self.number % self.row)}'
            return r
        if self.number % self.row == 0:
            r = "*" * self.row
            for i in range(self.number//self.row - 1):
                r += f'\\n{"*" * self.row}'
            return r

c_1 = Cell(15)
c_2 = Cell(3)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1*c_2)
print(c_1/c_2)
print(c_1.make_order(5))
print(c_1.make_order(4))

