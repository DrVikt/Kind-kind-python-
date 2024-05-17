#Подвиг 6. Объявите в программе следующий список названий нот:
#m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
#Затем, на вход программе подаются три целых числа в диапазоне от 1 до 7 в одну строчку через пробел: номера нот. Необходимо прочитать эти числа и сформировать строку с названиями прочитанных номеров нот, 
#следующих в строчку через пробел. Дополнительно перед нотами до и фа поставить символ диеза '#'.
#Реализовать программу с использованием тернарного условного оператора (он может применяться несколько раз).
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.3.6
#Sample Input:
#1 6 7
#Sample Output:
# #до ля си

# put your python code here
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())
a1 = '#' + m[a - 1] if (a == 1 or a == 4) else m[a - 1]
b1 = '#' + m[b - 1] if (b == 1 or b == 4) else m[b - 1]
c1 = '#' + m[c - 1] if (c == 1 or c == 4) else m[c - 1]
print(a1, b1, c1)