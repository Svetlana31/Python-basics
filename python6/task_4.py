#4. Реализуйте базовый класс Car.
#У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#А также методы: go, stop, turn(direction),которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#Для классов TownCar и WorkCar переопределите метод show_speed.
#При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#Выполните вызов методов и также покажите результат.
class Car():
    speed = 0
    color = None
    name = None
    is_police = bool()
    def __init__(self,speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'Автомобиль марки "{self.name}" (цвет "{self.color}") начал движение.'
    def stop(self):
        return "Автомобиль остановился."
    def turn(self, direction):
        self.direction = direction
        return f'Автомобиль "{self.name}" повернул {direction}.'
    def show_speed(self):
        return f'Скорость автомобиля "{self.name}" составляет {self.speed} км/ч.'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return ("Вы привышаете скорость!")
        else:
            return f'Скорость автомобиля "{self.name}" составляет {self.speed} км/ч.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return ("Вы привышаете скорость!")
        else:
            return f'Скорость автомобиля составляет "{self.speed}" км/ч.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


m = Car(50, "broun", "Mazda", False)
print(m.go(), m.show_speed(), m.turn("налево"), m.stop())
k = TownCar(40, "black", "KIA", False)
print(k.show_speed())
f = SportCar(150, "red", "Ferrari", False)
print(f.go(), f.show_speed())
h = WorkCar(50, "white", "Hyunday", False)
print(h.show_speed())
t = PoliceCar(60, "white", "Toyota", True)
print(t.turn("направо"), t.stop())
