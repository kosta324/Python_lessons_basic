# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player_name = input("Введите имя игрока: ")
player = {'name': player_name, 'health': 100, 'damage': 50, 'armor': 1.2}
enemy_name = input("Введите имя врага: ")
enemy = {'name': enemy_name, 'health': 100, 'damage': 50, 'armor': 1.2}


def attack(person1, person2):
    person2['health'] -= int(person1['damage']) / int(person2['armor'])


with open('{}_gamer.txt'.format(player_name), 'w') as file:
    for i in player:
        file.write("{} - {}\n".format(i, player[i]))

with open('{}_gamer.txt'.format(enemy_name), 'w') as file:
    for i in enemy:
        file.write("{} - {}\n".format(i, enemy[i]))


def game_log(person1, person2):
    attack(person1, person2)

    with open('{}_gamer.txt'.format(person1['name']), 'w') as file:
        for i in person1:
            file.write("{} - {}\n".format(i, person1[i]))

    with open('{}_gamer.txt'.format(person2['name']), 'w') as file:
        for i in person2:
            file.write("{} - {}\n".format(i, person2[i]))


while (True):
    game_log(player, enemy)
    if (enemy['health'] <= 0):
        print('Победил игрок {}, с оставшимися жизнями {}!'.format(player['name'], player['health']))
        break
    game_log(enemy, player)
    if (player['health'] <= 0):
        print('Победил игрок {}, с оставшимися жизнями {}!'.format(enemy['name'], enemy['health']))
        break
