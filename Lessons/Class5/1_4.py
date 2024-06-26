#Подвиг 8. На вход программе поступают номера телефонов с привязкой к именам в виде строк следующего формата:
#номер_1 имя_1
#номер_2 имя_2
#...
#номер_N имя_N
#В программе уже реализовано считывание всех строк и сохранение их в виде списка:
#lst_in = list(map(str.strip, sys.stdin.readlines()))
#На основе списка lst_in необходимо создать словарь d, где ключами будут имена, а значениями - список номеров телефонов для этого имени (ключа). Обратите внимание, что одному имени может принадлежать несколько разных номеров. Полученный словарь вывести командой:
#print(*sorted(d.items()))
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.1.8
#Sample Input:
#+71234567890 Сергей
#+71234567810 Сергей
#+51234567890 Михаил
#+72134567890 Николай
#Sample Output:
#('Михаил', ['+51234567890']) ('Николай', ['+72134567890']) ('Сергей', ['+71234567890', '+71234567810'])


import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
lst = [row.split() for row in lst_in]
d = {}
for i in lst:
        if i[1] in d:
                d[i[1]].append(i[0])
        else:
                d[i[1]] = [i[0]]
print(*sorted(d.items()))