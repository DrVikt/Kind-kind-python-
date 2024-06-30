#Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел. Необходимо прочитать эту строку и сохранить в какой-либо переменной.
#Напишите функцию get_list с одним параметром, которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для функции get_list, который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться в виде списка чисел при вызове декоратора.
#Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
#print(*lst)
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.11.3
#Sample Input:
#8 11 -5 4 3 10
#Sample Output:
#-5 3 4 8 10 11




# put your python code here
def show_menu(func):
    def wrapper(*args):
        r = sorted(func(*args))
        return r
    return wrapper


@show_menu
def get_list(ls):
    return list(map(int, ls.split()))


st = input()
lst = get_list(st)
print(*lst)