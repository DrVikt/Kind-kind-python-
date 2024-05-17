#Подвиг 4. Используя функцию range(), выведите на экран последовательность целых чисел 1, 4, 7, 10, 13, 16, 19 в одну строчку через пробел.

# put your python code here
lst = []
for i in range(1, 20, 3):
    lst.append(i)
print(*lst)