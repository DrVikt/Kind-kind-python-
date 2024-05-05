#Подвиг 7. Вводятся оценки студента (целые числа от 2 до 5) в одну строчку через пробел. На основе введенной строки формируется список командой:
#marks = list(map(int, input().split()))
#Необходимо вычислить средний балл и вывести его на экран с точностью до десятых (один знак после запятой).
#Sample Input:
#3 3 2 4 4 5 4 3 2
#Sample Output:
#3.3


# put your python code here
marks = list(map(int, input().split()))
lst = list(marks)
print(round(sum(lst)/len(lst),1))