#Подвиг 5. На вход программе подаются оценки студента (его ответов у доски по предмету "Информатика") в виде чисел от 2 до 5, записанных в одну строчку через пробел. 
#Необходимо прочитать эти числа. Затем, проверить, если студент имеет хотя бы одну двойку, то он не допускается до экзамена. Вывести на экран слово "ДОПУЩЕН", если студент не имеет ни одной двойки, иначе вывести "НЕ ДОПУЩЕН". 
#При реализации задачи используйте множество для определения наличия двойки.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.5.5
#Sample Input:
#3 4 4 5 2 3
#Sample Output:
#НЕ ДОПУЩЕН


# put your python code here
lst = list(map(int, input().split()))
print("НЕ ДОПУЩЕН" if 2 in set(lst) else "ДОПУЩЕН")