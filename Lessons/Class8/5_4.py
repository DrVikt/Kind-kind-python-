#Подвиг 4. На вход программе подается строка из слов, записанных через пробел. Необходимо прочитать эту строку, разбить на слова на основе полученного списка составить прямоугольную таблицу из трех столбцов и N строк 
#(число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить. Реализовать эту программу с использованием функции zip. Результат отобразить на экране в виде прямоугольной таблицы из слов, записанных через пробел (в каждой строчке).
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.5.4
#Sample Input:
#Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь
#Sample Output:
#Москва Уфа Тула
#Самара Омск Воронеж
#Владивосток Лондон Калининград



# put your python code here
lst = map(str, input().split())
z = zip(*[lst]*3)
for i in z:
    print(*i)