#Подвиг 5. На вход программе подается натуральное число n. Необходимо его прочитать и сформировать список с помощью list comprehension, состоящий из делителей числа n (включая и само число n). 
#Элементы полученного списка вывести в одну строчку через пробел.
#Ликбез: делителями числа n называются целые числа, которые делят n нацело (без остатка).
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.5
#Sample Input:
#10
#Sample Output:
#1 2 5 10


# put your python code here
a = int(input())
lst = [i for i in range(1, a + 1) if a % i == 0]
print(*lst)