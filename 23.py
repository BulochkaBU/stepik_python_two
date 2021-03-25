'''
Условие задачи:
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".

Sample Input:
\w denotes word character
No slashes here
Sample Output:
\w denotes word character
'''

# Code
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\\"
    match = re.search(pattern, line)
    if match is not None:
        print(line)
