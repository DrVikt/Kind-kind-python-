#Подвиг 4. На вход программе подается двумерный список размерностью 5 х 5 элементов, состоящий из нулей и в некоторых позициях единицы (см. пример ниже). В программе уже реализовано их чтение и сохранение в списке:
#s = sys.stdin.readlines()
#lst_in = [list(map(int, x.strip().split())) for x in s]
#Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и диагонали. То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести на экран "ДА", иначе "НЕТ".
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.6.4
#Sample Input:
#1 0 0 0 0
#0 0 1 0 1
#0 0 0 0 0
#0 1 0 1 0
#0 0 0 0 0
#Sample Output:
#ДА


import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
t = True
i = 0
while i < 4 and t:
    for j in range(len(lst_in[i])):
        if lst_in[i][j] == 1 and (0 < j < 4)  and (lst_in[i][j+1] + lst_in[i+1][j-1] + lst_in[i+1][j] + lst_in[i+1][j+1]) != 0 :
            t = False
            break
        elif lst_in[i][j] and (j == 0) and (lst_in[i][j + 1] + lst_in[i + 1][j] + lst_in[i+1][j+1]) != 0:
            t = False
            break
        elif lst_in[i][j] and (j == 4) and (lst_in[i + 1][j - 1] + lst_in[i + 1][j]) != 0:
            t = False
            break
    i += 1
pr = "ДА" if t else "НЕТ"
print(pr)