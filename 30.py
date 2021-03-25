'''
Условие задачи:
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
Файл с данными:
Crimes.csv
'''

# Code
import csv

r = []
c = 0
with open('crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if "2015" in row[2]:
            r.append(row[5])
for x in r:
    y = r.count(x)
    if y > c:
        c = y
    elif y == c:
        ans = x
with open("ans_crime.csv", 'w+') as w:
    writer = csv.writer(w)
    writer.writerow(ans.split())
