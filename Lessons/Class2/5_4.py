#Подвиг 4. Вводится адрес (каждое значение с новой строки) в формате: город, улица, номер дома (целое число), номер квартиры (целое число). 
#Сформировать строку по шаблону: "г. <город>, ул. <улица>, д. <номер дома>, кв. <номер квартиры>", используя F-строку. Результат вывести на экран.
#Sample Input:
#Москва
#Воздвиженка
#9
#1
#Sample Output:
#г. Москва, ул. Воздвиженка, д. 9, кв. 1


# put your python code here
a = str(input())
b = str(input())
c = int(input())
d = int(input())
print(f"г. {a}, ул. {b}, д. {c}, кв. {d}")