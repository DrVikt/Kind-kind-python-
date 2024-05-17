#Подвиг 4. На вход программе подается строка с названиями городов, записанных через пробел. Необходимо прочитать эту строку и сформировать список с помощью list comprehension, 
#содержащий названия городов длиной более пяти символов. Элементы полученного списка вывести в одну строчку через пробел.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.4
#Sample Input:
#Казань Уфа Москва Челябинск Омск Тур Самара
#Sample Output:
#Казань Москва Челябинск Самара


# put your python code here
lst = list(input().split())
lst = [lst[i] for i in range(len(lst)) if len(lst[i]) > 5 ]
print(*lst)