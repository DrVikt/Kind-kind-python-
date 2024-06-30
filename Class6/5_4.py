#Значимый подвиг 6. (Для закрепления предыдущего материала). Объявите в программе функцию с именем str_min, которая сравнивает две переданные строки (через два первых параметра) и возвращает минимальную из них 
#(то есть, выполняется лексикографическое сравнение строк). Затем, используя функциональный подход к программированию (то есть, более сложные функции реализуются путем вызова более простых), реализовать еще две аналогичные функции:
#    с именем str_min3 для поиска минимальной строки из трех переданных строк;
#    с именем str_min4 для поиска минимальной строки из четырех переданных строк.
#То есть, при реализации функций str_min3 и str_min4 следует использовать вызов функции str_min.
#P.S. Выполнять функции не нужно, только объявить.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.5.6



# put your python code here
def str_min(a,b):
    return a if a < b else b


def str_min3(a, b, c):
    return str_min(a,b) if str_min(a,b) < c else c


def str_min4(a, b, c, d):
    return str_min(a,b) if str_min(a,b) < str_min(c,d) else str_min(c,d)