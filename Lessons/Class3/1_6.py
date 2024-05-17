#Подвиг 6. На вход программе подается слово (строка). Необходимо прочитать это слово и проверить, что в нем присутствуют все три буквы: t, h и o (в произвольном порядке и хотя бы в одном экземпляре). 
#Реализовать программу следует с помощью одного условного оператора. Если искомая проверка проходит, вывести "ДА", иначе "НЕТ".
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.1.6
#Sample Input:
#Python
#Sample Output:
#ДА


# put your python code here
lst = list(input().lower())
if 't' in lst and 'h' in lst and 'o' in lst:
    print("ДА")
else:
    print("НЕТ"