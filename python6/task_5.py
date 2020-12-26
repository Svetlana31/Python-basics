#5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title = None
    def __init__(self, title=None):
        self.title = title
    def draw(self):
        return "Запуск отрисовки."

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Отрисовка {self.title}"

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Отрисовка {self.title}!"

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Отрисовка "{self.title}".'


a = Stationery()
print(a.draw())
b = Pen("ручкой")
print(b.draw())
c = Pencil("карандашом")
print(c.draw())
d = Handle("маркером")
print(d.draw())
