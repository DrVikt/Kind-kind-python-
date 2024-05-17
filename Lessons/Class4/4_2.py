#Подвиг 2. На вход программе подается строка с номером телефона. Ожидается следующий формат номера в строке:
#+7(xxx)xxx-xx-xx
#где x - это любая цифра. Число введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя). 
#Необходимо прочитать строку из входного потока и проверить, что она содержит номер телефона в соответствии с приведенным форматом. Вывести "ДА", если это так и "НЕТ" в противном случае.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.2
#Sample Input:
#+7(123)456-78-99
#Sample Output:
#ДА


# put your python code here
lst= input()
lst_sh = '+7(xxx)xxx-xx-xx'
for i in range(len(lst)):
    if (lst_sh[i] != 'x' and lst[i] == lst_sh[i]) or (lst_sh[i] == 'x' and lst[i].isdigit()):
        continue
    else:
        print("НЕТ")
        break
else:
    print("ДА")