#Подвиг 6. На вход программе подается строка (слаг). Прочитайте эту строку и замените в ней все подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-). #
#Результат преобразования строки выведите на экран. Программу реализовать при помощи цикла while.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.16
#Sample Input:
#osnovnye--metody-----slovarey
#Sample Output:
#osnovnye-metody-slovarey


# put your python code here
lst = input()
while '--' in lst :
    lst = lst.replace('--', '-')
print(lst) 