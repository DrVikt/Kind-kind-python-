#Подвиг 4. На вход программе подается строка с названиями городов, записанных через пробел. Прочитайте эту строку, сформируйте список из названий городов и выберите из этого списка один город случайным образом. Отобразите выбранный город на экране.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.3.4
#Sample Input:
#Тула Казань Смоленск Семипалатинск Уфа Москва Самара
#Sample Output:
#Казань



import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
lst = input().split()
print(random.choice(lst))