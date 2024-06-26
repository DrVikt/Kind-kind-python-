#Подвиг 7. Объявите в программе функцию, которая имеет один параметр, принимающий строку. Функция должна возвращать булево значение False, если длина переданной строки меньше 6 символов, иначе возвращать булево значение True.
#После объявления функции далее в программе прочитайте из входного потока строку с названиями городов, записанных через пробел. Сформируйте на основе прочитанной строки список cities из названий городов. Затем, используя генератор списка и ранее объявленную функцию, сформируйте новый список lst из названий городов с длинами не менее шести символов (города выбираются из списка cities). Результат отобразите на экране командой:
#print(*lst)
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.2.7
#Sample Input:
#Москва Уфа Пермь Самара Вологда
#Sample Output:
#Москва Самара Вологда


# put your python code here
def get_city(st):
    return True if len(st) > 5 else False


lst_in = input().split()
lst = [i for i in lst_in if get_city(i)]
print(*lst)