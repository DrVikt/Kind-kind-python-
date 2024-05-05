#Подвиг 4. Вводится строка со словами, разделенными пробелом. Необходимо первый пробел заменить на одинарную кавычку, а все остальные - на двойные. Результирующую строку отобразить на экране.
#Sample Input:
#My best friend is Python!
#Sample Output:
#My'best"friend"is"Python!


# put your python code here
a = str(input())
a = a.replace(" ", "\'", 1)
print(a.replace(" ", '\"'))