#Подвиг 5. Вводится вещественное число. Нужно определить, что его целая часть кратна 3. На экран вывести True,
#если кратно и False - в противном случае. Задача делается без использования условного оператора.
#Sample Input:
#78.34
#Sample Output:
#True


# put your python code here
import math
a = float(input())
a = math.floor(a)
print(a % 3 ==0)