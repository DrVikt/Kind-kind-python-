#Подвиг 8. На вход программе подаются два списка целых чисел одинаковой длины, каждый с новой строки. Необходимо их прочитать и каждый сохранить в своем отдельном списке. 
#Затем, с помощью list comprehension сформировать третий список, состоящий из суммы соответствующих пар чисел введенных списков. Элементы полученного списка вывести в одну строчку через пробел.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.8
#Sample Input:
#1 2 3 4 5
#6 7 8 9 10
#Sample Output:
#7 9 11 13 15


# put your python code here
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst = [lst1[i] + lst2[i] for i in range(len(lst1))]
print(*lst)