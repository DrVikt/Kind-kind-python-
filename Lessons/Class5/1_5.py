#Подвиг 9. На вход программе поступают целые положительные числа. Необходимо с помощью цикла реализовать их считывание, пока не встретится число 0. 
#В теле цикла для каждого прочитанного числа вычисляется квадратный корень (с точностью до сотых) и значение выводится на экран (в столбик). 
#С помощью словаря выполните кэширование данных так, чтобы при повторном вводе того же самого числа результат не вычислялся, а бралось ранее вычисленное значение (из словаря). При этом на экране должно выводиться:
#значение из кэша: <число>
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.1.9
#Sample Input:
#1
#2
#3
#3
#2
#4
#0
#Sample Output:
#1.0
#1.41
#1.73
#значение из кэша: 1.73
#значение из кэша: 1.41
#2.0


# put your python code here
a = int(input())
d = {}
while a != 0:
    if a in d:
        print('значение из кэша:', *d[a])
    else:
        b = round(a **0.5, 2)
        d[a] = [b]
        print(b)
    a = int(input())