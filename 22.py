'''
Условие задачи:
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:
zabcz
zzxzz
'''

# Code
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"z...z"
    match = re.search(pattern, line)
    if match is not None:
        print(line)
