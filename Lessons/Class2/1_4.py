#Подвиг 9. Написать программу ввода строки и формирования новой строчки вида: "Строка: <введенная строка>. Длина: <длина строки>".
#Результат сформированной строки вывести на экран.
#P. S. В программе F-строки не использовать.
#Sample Input:
#hello Balakirev
#Sample Output:
#Строка: hello Balakirev. Длина: 15



# put your python code here
a = str(input())
print(f'Строка: {a}. Длина: ' + str(len(a)))