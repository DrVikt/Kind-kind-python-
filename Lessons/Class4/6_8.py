#Подвиг 8. В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64. На вход программы подается натуральное число n. Необходимо его прочитать. 
#Затем определите, каким наименьшим количеством денежных купюр достоинством в 1, 2, 4, 8, 16, 32 и 64 можно выплатить сумму n? выведите на экран список купюр для формирования суммы n 
#(в одну строчку через пробел, начиная с наибольшей и заканчивая наименьшей). Предполагается, что имеется достаточно большое количество купюр всех достоинств.
#P.S. Программа может быть реализована и без вложенных циклов.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.6.8
#Sample Input:
#221
#
#Sample Output:
#64 64 64 16 8 4 1


# put your python code here
lst = [64,32,16,8,4,2,1]
a = int(input())
lst1 = []
for i in range(len(lst)):
    while a >= lst[i] and a > 0:
        a = a - lst[i]
        lst1.append(lst[i])
print(*lst1)