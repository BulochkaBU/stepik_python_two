'''
Условие задачи:
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".
Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
'''

# Code
import os
import os.path

os.chdir('main (1)')
a = []
for current_dir, dirs, files in os.walk('.'):
    for x in files:
        if x[-3:] == '.py':
            a.append(current_dir[2:])
s = set()
for x in a:
    s.add(x)
a = []
for x in s:
    a.append(x)
a.sort()
for x in a:
    x = str(x)
    with open('answer_main(1).txt', 'a') as i:
        i.write(x)
        i.write('\n')
