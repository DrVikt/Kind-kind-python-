#Подвиг 1. На вход программе подаются два вещественных числа, каждое с новой строки. Необходимо их прочитать и с помощью тернарного условного оператора вычислить наибольшее среди них и присвоить переменной d. 
#Полученное значение переменной d вывести на экран.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.3.1
#Sample Input:
#5.4
#-3.8
#Sample Output:
#5.4

# put your python code here
a = float(input())
b = float(input())
d = a if a > b else b
print(d)