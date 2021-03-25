'''
Условие задачи:
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:
Yes

Sample Input 2:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html
Sample Output 2:
No

Sample Input 3:
https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 3:
Yes
'''

# Code
import requests
import re

a = input()
b = input()
res_a = requests.get(a)
if res_a.status_code != 200:
    print("No")
ans = "No"
pattern = re.findall(r"https?://[^\"\s>]+", res_a.text)
for x in pattern:
    res_x = requests.get(x)
    pattern_2 = re.findall(r"https?://[^\"\s>]+", res_x.text)
    if b in pattern_2 and res_x.status_code == 200:
        ans = "Yes"
        break
print(ans)
