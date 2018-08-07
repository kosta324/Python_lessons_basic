
__author__ = 'Korotkov Konstantin'

name = input('Введите свое имя и фамилию: ')
age = int(input('Введите свой возраст: '))
weight = int(input('Введите свой вес: '))

check_weight = False
if weight < 50 or weight > 120:
    check_weight = True

if age < 30 and not(check_weight):
    print('хорошее состояние ')
elif age > 40 and check_weight:
    print('следует обратится к врачу! ')
elif check_weight:
    print('следует заняться собой ')
else:
    print('да Вы просто Рембо) ')
