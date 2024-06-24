#Подвиг 7. На вход программе подаются номера телефонов, записанные в одну строчку через пробел, с разными кодами стран: +7, +6, +2, +4 и т.д. 
#Необходимо прочитать строку и на ее основе сформировать словарь d. Ключами словаря должны быть коды (строки: +7, +6, +2 и т. п.), 
#а значениями список номеров в виде строк (следующих в том же порядке, что и в исходной строке) с соответствующими кодами. Полученный словарь вывести командой:
#print(*sorted(d.items()))
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.1.7
#Sample Input:
#+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
#Sample Output:
#('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])



# put your python code here
lst = input().split()
d = {}
for x in lst:
    if x[:2] in d:
        d[x[:2]].append(x)
    else:
        d[x[:2]]=[x]
print(*sorted(d.items()))