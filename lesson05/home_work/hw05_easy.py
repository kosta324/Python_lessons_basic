# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys

for i in range(9):
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(i + 1))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая папка существует ' + dir_path)

for i in range(9):
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(i + 1))
    try:
        os.rmdir(dir_path)
    except OSError:
        print('Папку нельзя удалить ' + dir_path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for i, dir, file in os.walk(os.getcwd()):
    print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

