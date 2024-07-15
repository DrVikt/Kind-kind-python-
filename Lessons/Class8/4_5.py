#Подвиг 5. На вход программе подается строка с email-адресами, записанных через пробел. Нужно прочитать эту строку и среди email-адресов оставить только корректно записанные адреса. 
#Полагается, что к таким относятся те, что используют только латинские буквы, цифры и символ подчеркивания. Также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).
#Результат отобразить в виде строки email-адресов, записанных через пробел в порядке их следования в исходной строке.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.4.5
#Sample Input:
#abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
#Sample Output:
#abc@it.ru biba123@list.ru sc_lib@list.ru


# put your python code here
a = input().split()
b = 'abcdefghijklmnopqrstuvwxyz@._0123456789'
def check_email(x):
    if x.find('@') < x.find('.'):
        st=''
        for k in x:
            if k in b:
                st += k
            else:
                st =''
                break
        return st


print(*filter(check_email, a))