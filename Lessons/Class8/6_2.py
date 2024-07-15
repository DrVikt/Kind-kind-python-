#Подвиг 3. Объявите в программе функцию со следующей сигнатурой:
#def get_sort(d): ...
#На входе этой функции (в параметре d) ожидается словарь формата (пример):
#d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
#Функция должна выполнить сортировку ключей словаря d по убыванию (лексикографическая сортировка строк) и возвратить список из соответствующих значений ключей словаря. Сам словарь d при этом должен оставаться неизменным. Например, для указанного словаря d, результатом работы функции должен быть список:
#['дерево', 'лошадь', 'собака', 'кот', 'книга']
#В программе нужно реализовать только функцию get_sort, вызывать ее не нужно и что-либо выводить на экран.
#Подсказка: список в функции get_sort лучше всего формировать с помощью генератора списков.




def get_sort(d):
    c = sorted(d.items(), reverse=True )
    lst = [b for a,b in c]
    return lst