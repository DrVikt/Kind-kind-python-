#Подвиг 2. На вход программы подаются два целых положительных числа n и m, записанных через пробел, причем, n < m. Необходимо прочитать эти числа и вывести в одну строку через пробел 
#квадраты целых чисел в диапазоне [n; m]. Программу реализовать при помощи цикла while.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.1.2
#Sample Input:
#2 4
#Sample Output:
#4 9 16

# put your python code here
a, b = map(int, input().split())
lst = []
while a <= b:
    lst.append(a ** 2)
    a += 1
print(*lst)