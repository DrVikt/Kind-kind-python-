#Подвиг 5. На вход программе подаются целые числа, записанные в одну строчку через пробел. Необходимо прочитать эти числа и сохранить в списке (в виде чисел, а не строк). 
#Затем, с помощью цикла for перебрать полученный список и просуммировать все нечетные значения. Результат (сумму) вывести на экран.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.3.5
#Sample Input:
#8 11 -2 4 0 13 19 12 7
#Sample Output:
#50


# put your python code here
lst = list(map(int, input().split()))
s = 0
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        s += lst[i]
print(s)