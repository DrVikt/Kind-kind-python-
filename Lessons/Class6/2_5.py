#Подвиг 5. Объявите в программе функцию с одним параметром для проверки переданного числа на нечетность. Функция должна возвращать булево значение True, если переданное число нечетное, и False в противном случае. 
#После объявления функции далее в программе прочитайте последовательность целых чисел, подаваемых на вход программе, с помощью команды:
#lst_d = list(map(int, input().split()))
#Затем, используя генератор списков и объявленную ранее функцию, сформируйте список lst из нечетных значений на основе списка lst_d. Результат отобразите на экране командой:
#print(*lst)
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.2.5
#Sample Input:
#8 11 -15 3 2 10
#Sample Output:
#11 -15 3


# put your python code here
lst_d = list(map(int, input().split()))
def get_even(a):
    return a % 2 != 0


lst = [i for i in lst_d if get_even(i)]
print(*lst)