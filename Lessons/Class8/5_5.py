#Подвиг 5. На вход программе подается строка. Требуется ее прочитать и сформировать N=10 пар кортежей в формате:
#(символ, порядковый индекс)
#Например, подается строка "Sergey Balakirev", на выходе формируются кортежи (сохраненные в списке):
#[('S', 0), ('e', 1), ('r', 2), ('g', 3), ('e', 4), ('y', 5), (' ', 6), ('B', 7), ('a', 8), ('l', 9)]
#Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. То есть, число пар может быть 10 и менее. Используя функцию zip сформируйте указанные кортежи и сохраните их списке с именем lst.
#P.S. Программа ничего не должна отображать на экране, только формировать список lst из кортежей.

# считывание строки в переменную s (эту переменную в программе не менять)
s = input()

# здесь продолжайте программу
lst_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = list(zip(s,lst_in))