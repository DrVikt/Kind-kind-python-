#Подвиг 10. На вход программе подается натуральное число n. Прочитайте это число и вычислите сумму всех натуральных чисел меньше n, которые кратны или 3 или 5. Результат (сумму) выведите на экран.
#Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.3.10
#Sample Input:
#21
#Sample Output:
#98


# put your python code here
n = int(input())
s = 0
for i in range(1, n):
    if (i % 3 == 0 or i % 5 == 0):
        s += i
print(s)