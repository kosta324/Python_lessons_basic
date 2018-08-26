# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, damage, armor):
        return damage // armor

    def attack(self, who_defend):
        damage = self._calculate_damage(self.damage, who_defend.armor)
        who_defend.health -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(self.name, who_defend.name, damage,
                                                                        who_defend.health))


class Player(Person):
    pass


class Enemy(Person):
    pass


def start_game():
    player_name = input('Введите имя: ')
    enemy_name = input('Введите имя: ')
    player = Player(player_name, 100, 50, 1.2)
    enemy = Enemy(enemy_name, 100, 50, 1.2)
    last_attacker = player

    while player.health > 0 and enemy.health > 0:
        if last_attacker == player:
            enemy.attack(player)
            last_attacker = enemy
        else:
            player.attack(enemy)
            last_attacker = player

    if player.health > 0:
        print('Игрок победил!')
    else:
        print('Враг победил!')


start_game()
