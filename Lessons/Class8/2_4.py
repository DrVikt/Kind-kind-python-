#Подвиг 4. На вход программе подается натуральное число N, которое необходимо прочитать и сохранить через переменную. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:
#from string import ascii_lowercase, ascii_uppercase
#chars = ascii_lowercase + ascii_uppercase
#объявите функцию-генератор с одним параметром max_size, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной max_size = N символов. Например, при N=6 адрес может выглядеть так: SCrUZo@mail.ru
#Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно. Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
#Подсказка: для формирования случайного индекса для выбора символа из строки chars, используйте функцию randint модуля random:
#import random
#random.seed(1)
#indx = random.randint(0, len(chars)-1)
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.2.4
#Sample Input:
#8
#Sample Output:
#iKZWeqhF@mail.ru
#WCEPyYng@mail.ru
#FbyBMWXa@mail.ru
#SCrUZoLg@mail.ru
#ubbbPIay@mail.ru



# put your python code here
from string import ascii_lowercase, ascii_uppercase
import random

random.seed(1)
chars = ascii_lowercase + ascii_uppercase

N = int(input())


def gen_email():
    indx = random.randint(0, len(chars) - 1)
    yield chars[indx]


k = 0
while k < 5:
    lst = ''
    for i in range(N):
        lst += next(gen_email())
    print(f"{lst}@mail.ru")
    k += 1