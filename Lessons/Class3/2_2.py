#Подвиг 2. На вход программе подаются три целых числа, записанных в одну строку через пробел. Необходимо прочитать их и определить наименьшее среди прочитанных чисел. Наименьшее найденное значение вывести на экран.
#P.S. Программу реализовать следует, используя условный оператор, без использования функции min.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.2.2
#Sample Input:
#8 11 -1
#Sample Output:
#-1

# put your python code here
a, b, c = map(int, input().split())
if a > b:
    if b > c:
        print(c)
    else:
        print(b)
else:
    if a > c:
        print(c)
    else:
        print(a)