#Подвиг 4. На вход программе подается строка с названиями городов, записанных в одну строчку через пробел. Прочитайте эту строку и сформируйте на ее основе список из названий городов. 
#Необходимо определить, что в этом списке все города имеют длину более 5 символов. Если это так, то на экран вывести строку "ДА", иначе строку "НЕТ". Программу реализовать с использованием цикла while и оператора break. 
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.2.4
#Sample Input:
#Самара Ульяновск Новгород Воронеж
#Sample Output:
#ДА


# put your python code here
lst = list(input().split())
i = 0
while i < len(lst):
    if len(lst[i]) < 6:
        print("НЕТ")
        break
    i += 1    
else:
    print("ДА")