#Подвиг 2. Объявите функцию, которая переводит символы строки в нижний регистр (малые буквы) и возвращает результат. 
#Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
#Пример заключения строки "python" в тег h1:
#<h1>python</h1>
#Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для строки s, прочитанной из входного потока:
#s = input()
#Результат работы декорированной функции отобразите на экране.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.12.2
#Sample Input:
#Декораторы - это классно!
#Sample Output:
#<div>декораторы - это классно!</div>


# put your python code here
s = input()
def tag_decor(tag = "h1"):
    def decor_string(func):
        def wrapper(*args):
            c = f'<{tag}>{func(*args)}</{tag}>' 
            return c
        return wrapper
    return decor_string                     

@tag_decor(tag = 'div')
def get_lower(st):
    return st.lower()
                         

print(get_lower(s))
                    