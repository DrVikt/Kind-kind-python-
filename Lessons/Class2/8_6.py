#Подвиг 8. Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать их в список lst , затем, удалить последнее значение и если оно нечетное, 
#то в список (в конец) добавить True, иначе - False. Отобразить полученный список на экране командой:
#print(*lst)
#Реализовать программу без использования условного оператора.
#Sample Input:
#8 11 0 3 5 6
#Sample Output:
#8 11 0 3 5 False


# put your python code here
lst = list(map(int, input().split()))
end = lst.pop()
lst.append(end %2 != 0)
print(*lst)