#Подвиг 2. Объявите в программе функцию с именем get_even, которая способна принимать произвольное количество чисел в качестве аргументов. Например:
#get_even(1, 2, 3, -5, 10, 8)
#Функция должна возвращать список, составленный только из четных переданных ей значений.
#P.S. Функцию вызывать не нужно, только определить.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.5.2
#Sample Input:
#45 4 8 11 12 0
#Sample Output:
#4 8 12 0




# put your python code here
def get_even(*args):
    return [i for i in args if i  %2 ==0]