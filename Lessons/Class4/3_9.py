#Подвиг 9. На вход программе подается строка с названиями городов, записанных в одну строчку через пробел. Необходимо прочитать эту строку и сформировать список из названий городов. 
#Переберите полученный список с помощью цикла for и определите, начинается ли название следующего города на последнюю букву предыдущего города в списке. Если последними встречаются буквы 'ь', 'ъ', 'ы', 
#то берется следующая с конца буква. Вывести на экран "ДА", если последовательность удовлетворяет этому правилу и "НЕТ" в противном случае.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.3.9
#Sample Input:
#Москва Астрахань Новгород Димитровград Душанбе
#Sample Output:
#ДА


# put your python code here
lst = input().lower().split()
for i in range(0, len(lst) - 1):
    lst[i] = lst[i].strip('ьъы')
    if lst[i + 1][0] != lst[i][-1]:
            print("НЕТ")
            break
else:
    print("ДА")