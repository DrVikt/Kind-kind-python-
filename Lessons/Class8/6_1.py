#Подвиг 2. На вход программе поступают целые числа, записанные через пробел. Прочитайте эту строку с числами и преобразуйте ее сначала в список из целых чисел, а затем список в кортеж из целых чисел. 
#То есть, в программе будет две разные коллекции: список и кортеж. Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно, а иначе - примените функцию sorted.
#На экран ничего выводить не нужно, только сформировать две отсортированные коллекции: lst (список) - результат сортировки списка; tp_lst (кортеж) - результат сортировки кортежа.
#P. S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.6.2
#Sample Input:
#-2 -1 8 11 4 5 
#Sample Output:
#True


# ввод строки в переменную s (переменную в программе не менять)
s = input()

# здесь продолжайте писать программу
lst = list(map(int, s.split()))
lst.sort()
tp_lst = tuple(sorted(tuple(map(int, s.split()))))