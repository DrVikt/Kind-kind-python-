#Подвиг 1. На вход программе поступает строка с наименованиями рек, записанных через пробел. Необходимо их прочитать и отсортировать названия рек в порядке убывания их длин строк (названий). 
#Результат вывести в одну строчку через пробел.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.7.1
#Sample Input:
#Лена Енисей Волга Дон
#Sample Output:
#Енисей Волга Лена Дон



# put your python code here
lst_in = input().split()
print(*sorted(lst_in, key = len, reverse = True))