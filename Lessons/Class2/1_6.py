#Подвиг 11. С клавиатуры вводятся две буквы (в одну строку через пробел). Вывести на экран следующую строку:
#"Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"
#Sample Input:
#a z
#Sample Output:
#Коды: a = 97, z = 122



# put your python code here
a, b = map(str, input().split())
print(f'Коды: {a} = ' + str(ord(a)) + f', {b} = ' + str(ord(b)))