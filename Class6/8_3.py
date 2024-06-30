#Подвиг 4. Объявите анонимную (лямбда) функцию для вычисления модуля числа (то есть, отрицательные числа нужно делать положительными). Вызовите эту функцию для числа x, которое следует прочитать из входного потока командой:
#x = float(input())
#Отобразите результат работы функции на экране.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.8.4
#Sample Input:
#-5.6
#Sample Output:
#5.6


# put your python code here
x = float(input())
r = lambda x: abs(x)
print(r(x))