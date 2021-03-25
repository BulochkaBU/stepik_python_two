'''
Условие задачи:
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line

Sample Input:
catcat
cat and cat
catac
cat
ccaatt
Sample Output:
catcat
cat and cat
'''

# Code
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\Bcat"
    match = re.search(pattern, line)
    if match is not None:
        print(line)
