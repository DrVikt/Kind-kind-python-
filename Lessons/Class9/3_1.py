#Подвиг 2. На вход программе подаются два натуральных числа a, b (a < b), записанных через пробел. Прочитайте их и выполните генерацию вещественной случайной величины в диапазоне [a; b). Округлите результат до сотых и выведите его на экран.
#Ликбез: квадратная скобка - граница включается в диапазон; круглая скобка - граница исключается из диапазона.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.3.2
#Sample Input:
#-4 5
#Sample Output:
#-2.79



import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
a,b = map(int, input().split())
print(round(random.uniform(a, b), 2))