#Подвиг 5. На вход программе подается строка, содержащая латинские символы, пробелы и цифры. Необходимо прочитать эту строку и выделить из нее все неповторяющиеся цифры (символы от 0 до 9). 
Выведите на экран все найденные уникальные цифры в одну строчку через пробел в порядке возрастания их значений. Если цифры отсутствуют, то вывести строку "НЕТ".
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.4.5
Sample Input:
Python 3.9.11 - best language!
Sample Output:
1 3 9


# put your python code here
a = set(input())
a = set(i for i in a if i.isdigit())
print( *sorted(a) if len(a) != 0 else ["НЕТ"])
