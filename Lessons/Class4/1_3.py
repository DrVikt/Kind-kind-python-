#Подвиг 4. На вход программы подается целое положительное число n. Прочитайте это число, а затем, вычислите и выведите на экран следующую сумму с точностью до тысячных (три знака после запятой):
#S=1+12+13+...+1n
#S=1+21​+31​+...+n1​
#Программу реализовать при помощи цикла while.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.1.4
#Sample Input:
#8
#Sample Output:
#2.718


# put your python code here
a = int(input())
i = 0
s = 0
while i < a :
    i += 1
    s +=(1 / i)
print(round(s, 3)) 