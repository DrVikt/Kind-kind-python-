#Подвиг 9. Вводится строка, состоящая из слов, разделенных пробелом. Необходимо подсчитать число слов в этой строке и результат (число) отобразить на экране.
#Sample Input:
#I love Python
#Sample Output:
#3


# put your python code here
a = str(input())
print(a.count(' ') + 1)