#Подвиг 5. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "ra". То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False в противном случае.
#Вызовите эту функцию для строки s, которую следует прочитать из входного потока командой:
#s = input()
#Отобразите результат работы функции на экране.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.8.5
#Sample Input:
#abrakadabra
#Sample Output:
#True


# put your python code here
s = input()
b = lambda s: "ra" in s

print(b(s))