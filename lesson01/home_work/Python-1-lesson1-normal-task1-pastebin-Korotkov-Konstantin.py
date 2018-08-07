
__author__ = 'Korotkov Konstantin'

namber = int(input('Введите число больше 0, но меньше 10: '))
while namber <= 0 or namber >= 10:
    namber = int(input('Число не верное, введите заново число больше 0, но меньше 10: '))
print('Квадрат числа равен:', namber**2)
