#Подвиг 2. Используя функцию range(), выведите на экран последовательность целых чисел -10, -9, -8, ..., 0 в одну строчку через пробел.


# put your python code here
lst = []
for i in range(10, -1, -1):
    lst.append(i)
print(*lst)     