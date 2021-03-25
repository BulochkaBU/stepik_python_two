'''
Условие задачи:
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:
blabla is a tandem repetition
123123 is good too
go go
aaa
Sample Output:
blabla is a tandem repetition
123123 is good too
'''

# Code
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b(.*\B)\1\b"
    match = re.search(pattern, line)
    if match is not None:
        print(line)
