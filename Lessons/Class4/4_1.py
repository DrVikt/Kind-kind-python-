#Подвиг 1. На вход программе подается строка. Необходимо ее прочитать и найти в ней все индексы строкового фрагмента "ра". Выведите найденные индексы на экран в одну строчку через пробел. 
#Если же фрагмент "ра" отсутствует в строке, то вывести -1.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.1
#Sample Input:
#Барабанщик бил бой в барабан
#Sample Output:
#2 23


# put your python code here
a = input()
s = ''
k = a.find('ра')
if k < 0:
    print(k)
else:
    s += (str(k) + ' ')
    for i in range(len(a)):
        k = a.find('ра', k + 1)
        if k > 0:
            s += (str(k)+' ')
        else:
            break
    print(s)