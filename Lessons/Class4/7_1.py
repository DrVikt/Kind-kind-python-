#Подвиг 1. На вход программе подаются вещественные числа, записанные через пробел. Необходимо их прочитать и сохранить в списке lst. Затем, используя list comprehension (генератора списков) 
#сформировать новый список lst_abs из модулей чисел списка lst (в итоговом списке должны храниться именно числа, а не строки). Список lst_abs вывести на экран командой:
#print(lst_abs)
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.1 
#Sample Input:
#5.56 -8.7 1.0 3.14 77.845
#Sample Output:
#[5.56, 8.7, 1.0, 3.14, 77.845]


# put your python code here
lst_in = list(map(float, input().split()))
lst = [float(abs(d)) for d in lst_in]
print(lst)