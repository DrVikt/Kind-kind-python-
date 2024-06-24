#Подвиг 8. На вход программе подаются названия городов, каждое с новой строки. Необходимо в цикле читать эти названия, пока не встретится строка "q". 
#С помощью множества определить общее уникальное число городов, которые читались в программе (за исключением "q"). На экран вывести это число.
#P.S. Из коллекций при реализации программы использовать только множества.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.4.8
#Sample Input:
#Уфа
#Москва
#Тверь
#Екатеринбург
#Томск
#Уфа
#Москва
#q
#Sample Output:
#5


# put your python code here
d = set()
i = input()
while i != 'q':
    d.add(i)
    i = input()
print(len(d))