#Подвиг 5. На вход программе подается четырехзначное число, которое нужно прочитать из входного потока. Проверить, что это число оканчивается на цифру 7. 
#Вывести на экран "ДА", если это так, и "НЕТ" в противном случае.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.1.5
#Sample Input:
#8117
#Sample Output:
#ДА


# put your python code here
lst = list(input())
if int(lst[-1]) == 7:
    print("ДА")
else:
    print("НЕТ")