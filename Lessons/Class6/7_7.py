#Великий подвиг 8. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и сохранить в списке. Затем, выполнить сортировку этого списка по возрастанию с помощью алгоритма сортировки слиянием. 
#Функция должна возвращать новый отсортированный список.
#Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде последовательности чисел, записанных через пробел.
#Подсказка: для разбиения списка и его последующей сборки используйте рекурсивные функции.
#P. S. Теория сортировки в видео предыдущего шага.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.7.8
#Sample Input:
#8 11 -6 3 0 1 1
#Sample Output:
#-6 0 1 1 3 8 11



# put your python code here
def get_merge(ls1, ls2):
    lst = []
    i = 0
    j = 0
    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            lst.append(ls1[i])
            i += 1
        else:
            lst.append(ls2[j])
            j += 1
    return lst + ls1[i:] + ls2[j:]


def get_split(lst):
    c = int(len(lst)/2)
    lst1 = lst[:c]
    lst2 = lst[c:]
    if len(lst1) > 1:
        lst1 = get_split(lst1)
    if len(lst2) > 1:
        lst2 = get_split(lst2)
    lst = get_merge(lst1, lst2)
    return lst


lst_in = list(map(int, input().split()))
print(*get_split(lst_in))