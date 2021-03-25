'''
Условие задачи:
Вашей программе будет доступна функция foo, которая может бросать исключения.
Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.
Пример решения, которое вы должны отправить на проверку.
try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
Подсказка: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''

# Code
try:
    foo()
except ZeroDivisionError as e:
    print("ZeroDivisionError")
except ArithmeticError as  e:
    print("ArithmeticError")
except AssertionError as r:
    print("AssertionError")
