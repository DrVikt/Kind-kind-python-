#Подвиг 2. На вход программе поступает строка из целых чисел, записанных через пробел. Необходимо прочитать эту строку. Затем, с помощью функции map преобразовать эту строку в список целых чисел, взятых по модулю. 
#Сформируйте именно список lst из таких чисел. Отобразите его на экране командой:
#print(*lst)
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.3.2
#Sample Input:
#-5 6 8 11 -10 0
#Sample Output:
#5 6 8 11 10 0


# put your python code here
lst = map(int, input().split())
lst = map(abs, lst)
print(*lst)