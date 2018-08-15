# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

list_1 = ("Саша", "Ваня", "Леша", "Миша", "Костя")
list_2 = (100000, 200000, 300000, 400000, 600000)
dict_1 = (dict(zip(list_1, list_2)))
file = open('salary.txt', 'w')
for i in dict_1:
    file.write("{} - {}\n".format(i, dict_1[i]))
file.close()
file = open('salary.txt')
for line in file:
    name, salary = line.split('-')
    salary = int(salary)
    if (salary <= 500000):
        print("{} - {}".format(name.upper(), salary * 0.87))
file.close()
