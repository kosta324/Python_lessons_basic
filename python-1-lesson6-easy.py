# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала...'.format(self.name))

    def stop(self):
        print('Машина {} остановилась...'.format(self.name))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} повернула {}'.format(self.name, self.direction))


class SportCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала...'.format(self.name))

    def stop(self):
        print('Машина {} остановилась...'.format(self.name))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} повернула {}'.format(self.name, self.direction))


class WorkCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала...'.format(self.name))

    def stop(self):
        print('Машина {} остановилась...'.format(self.name))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} повернула {}'.format(self.name, self.direction))


class PoliceCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала...'.format(self.name))

    def stop(self):
        print('Машина {} остановилась...'.format(self.name))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} повернула {}'.format(self.name, self.direction))


car_1 = TownCar(180, 'black', 'Toyota', False)
car_2 = SportCar(280, 'white', 'Ferrary', False)
car_3 = WorkCar(80, 'Green', 'Zil', False)
car_4 = PoliceCar(250, 'Blue', 'Lada', True)
car_1.go()
car_2.go()
car_3.stop()
car_4.turn('в лево')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self):
        print('Машина {} поехала...'.format(self.name))

    def stop(self):
        print('Машина {} остановилась...'.format(self.name))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} повернула {}'.format(self.name, self.direction))


class CityCar(Car):
    def __init__(self, color, name, speed):
        super().__init__(color, name)
        self.speed = speed

    def gas(self):
        print('Машина {} заправляется...'.format(self.name))


car_5 = Car('Red', 'Nissan')
car_6 = CityCar('Pink', 'Volvo', 150)
car_6.gas()

