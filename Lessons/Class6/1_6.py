#Подвиг 8. Объявите в программе функцию с одним параметром, которая проверяет корректность переданного ей email-адреса в виде строки. 
#Полагается, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит "ДА", иначе "НЕТ".
#После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.1.8
#Sample Input:
#sc_lib@list.ru
#Sample Output:
#ДА

# put your python code here
ch = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y', 'b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z','@', '.'}
    
def control_email(a):
    k = True
    if a.count('@') == 1 and a.count('.') == 1:
        for i in a:
            if i in ch:
                continue
            else:
                k = False
    else:
        k = False
    print("ДА" if k ==True else "НЕТ")



control_email(input().lower())