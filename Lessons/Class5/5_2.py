#Подвиг 2. На вход программе подаются два списка целых чисел, каждый с новой строки (в строке наборы чисел следующих через пробел). 
#Необходимо прочитать эти наборы чисел и сохранить их в отдельных списках (или кортежах). Затем, с помощью множеств(а) выбрать уникальные числа, присутствующие в первом списке, но отсутствующие во втором. 
#Результат выведите на экран в виде строки чисел, записанных по возрастанию через пробел, используя команду (здесь s - это множество, содержащее уникальные числа):
#print(*sorted(s))
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.5.2
#Sample Input:
#8 5 3 5 -3 1
#1 2 3 4
#Sample Output:
#-3 5 8


# put your python code here
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
s = set(lst1) - set(lst2)
print(*sorted(s))