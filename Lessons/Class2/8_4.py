#Подвиг 5. В одну строчку через пробел вводятся: имя, отчество и фамилия. Необходимо представить эти данные в виде новой строки в формате: Фамилия И.О. (Например, Сергей Михайлович Балакирев -> Балакирев С.М.).
#Sample Input:
#Сергей Михайлович Балакирев
#Sample Output:
#Балакирев С.М.


# put your python code here
lst = list(input().split())
print(lst[2], lst[0][0] + "." + lst[1][0] + ".")