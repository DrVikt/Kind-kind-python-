#Подвиг 8. Гелевая ручка стоит x рублей. Сегодня магазин предоставляет скидку в 10% на каждую купленную ручку.
#Какое наибольшее количество таких ручек можно будет купить на 500 рублей? Результат выведите в консоль в виде целого числа.
#Sample Input:
#20
#Sample Output:
#27


# ввод данных
x = int(input())

# здесь продолжите программу
import math
print(math.floor(500/(x*(1 - 0.1))))