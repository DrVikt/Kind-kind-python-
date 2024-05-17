#Подвиг 3. Используя функцию range(), выведите на экран последовательность целых чисел -10, -8, -6, -4, -2 в одну строчку через пробел.

# put your python code here
lst = []
for i in range(-10, 0, 2):
    lst.append(i)
print(*lst)