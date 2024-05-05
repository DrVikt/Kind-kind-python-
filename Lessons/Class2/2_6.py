#Подвиг 8. Из введенной строки отобразить первые пять символов в обратном порядке. Полагается, что введенная строка имеет минимум пять символов.
#Sample Input:
#abrakadabra
#Sample Output:
#karba


# put your python code here
a = str(input())
print(a[4::-1])