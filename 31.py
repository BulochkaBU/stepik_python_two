'''
Условие задачи:
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true
Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502
Пример выходного файла:
Interesting
Boring
Interesting
Boring
'''

# Code
import requests
import json

with open("dataset_24476_3.txt", 'r') as f:
    a = f.read().strip().split()
for x in a:
    api_url = f'http://numbersapi.com/{x}/math?json=true'
    res = requests.get(api_url)
    data = res.json()
    print(data)
    with open('ans_num_i_b.txt', 'a')as f:
        if data['found'] == False:
            f.write('Boring\n')
        if data['found'] == True:
            f.write('Interesting\n')
