#Подвиг 3. На вход программы подается вещественное число: стоимость одной книги x рублей. Необходимо прочитать это число и вывести на экран в одну строчку через пробел 
#стоимости 2, 3, ... 10-ти таких книг с точностью до десятых. Программу реализовать при помощи цикла while.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.1.3
#Sample Input:
#34.6
#Sample Output:
#69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0


# put your python code here
a = round(float(input()), 1)
lst=[]
i = 1
while i < 10 :
    i += 1
    lst.append(round(a * i, 1))
print(*lst)