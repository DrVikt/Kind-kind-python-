#Подвиг 3. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и сохранить в виде списка (или кортежа). Затем, объявить рекурсивную функцию с именем get_rec_sum для вычисления 
#суммы прочитанных чисел. То есть, функция get_rec_sum в итоге должна возвращать значение суммы. (Выводить на экран она ничего не должна). Первым параметром в функцию следует передавать список чисел. Остальные параметры 
#продумайте самостоятельно.
#Вызовите функцию get_rec_sum и выведите на экран значение суммы, которое она вернула.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.7.3
#Sample Input:
#8 11 -5 4 3
#Sample Output:
#21


# put your python code here
lst_in = list(map(int, input().split()))


def get_rec_sum(lst):
    a = 0
    if len(lst) > 1:
        a = get_rec_sum(lst[1:])
    return lst[0] + a


print(get_rec_sum(lst_in))