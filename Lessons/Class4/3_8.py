#Подвиг 8. На вход программе подается натуральное число n. Прочитайте это число и с помощью цикла for определите является ли оно простым (то есть, делится нацело только на само себя и на 1). 
#Вывести на экран строку "ДА", если n простое и строку "НЕТ" в противном случае.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.3.8
#
#Sample Input:
#11
#Sample Output:
#ДА


# put your python code here
a = int(input())
for i in range (2, a):
    if a % i == 0:
        print("НЕТ")
        break
else:
    print("ДА")