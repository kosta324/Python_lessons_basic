# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class Fabricate:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def buy(self):
        print('Покупаем материал для игрушки: {} ...'.format(self.name))

    def made(self):
        print('Шьем игрушку типа: {} ...'.format(self.model))

    def coloring(self):
        print('Красим игрушку в {} цвет...'.format(self.color))

    def finishing(self):
        return Toy(self.name, self.color, self.model)


class Toy(Fabricate):
    def sale(self):
        print('Отправляем на продажу игрушку: {}, цвет: {}, тип: {}'.format(self.name, self.color, self.model))


order = Fabricate('Винни-пух', 'бурый', 'медведь')
order.buy()
order.made()
order.coloring()
toy = order.finishing()
toy.sale()


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Bear(Fabricate):
    def finishing_bear(self):
        return BearToy(self.name, self.color, self.model)


class Elefant(Fabricate):
    def finishing_elefant(self):
        return ElefantToy(self.name, self.color, self.model)


class Rabbit(Fabricate):
    def finishing_rabbit(self):
        return RabbitToy(self.name, self.color, self.model)


class BearToy(Toy):
    def sale(self):
        print('Продаем медведя {}, цвет: {}'.format(self.name, self.color))


class ElefantToy(Toy):
    def sale(self):
        print('Продаем слона {}, цвет: {}'.format(self.name, self.color))


class RabbitToy(Toy):
    def sale(self):
        print('Продаем кролика {}, цвет: {}'.format(self.name, self.color))


order_bear = Bear('Винни-пух', 'бурый', 'медведь')
order_bear.buy()
order_bear.made()
order_bear.coloring()
order_elefant = Elefant('Данди', 'розовый', 'слон')
order_elefant.buy()
order_elefant.made()
order_elefant.coloring()
order_rabbit = Rabbit('Бакс Банни', 'серый', 'кролик')
order_rabbit.buy()
order_rabbit.made()
order_rabbit.coloring()
bear = order_bear.finishing_bear()
elefant = order_elefant.finishing_elefant()
rabbit = order_rabbit.finishing_rabbit()
bear.sale()
elefant.sale()
rabbit.sale()
