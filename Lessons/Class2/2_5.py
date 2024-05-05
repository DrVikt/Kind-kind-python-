#Подвиг 7. Вводятся две строки (каждая с новой строчки). Из первой строки выделить все символы с четными индексами, а из второй - с нечетными. Объединить строки через пробел и вывести на экран.
#Sample Input:
#Hello
#Python
#Sample Output:
#Hlo yhn


# put your python code here
a = str(input())
b = str(input())
print(a[::2], b[1::2])