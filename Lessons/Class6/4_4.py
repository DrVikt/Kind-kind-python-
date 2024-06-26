#Подвиг 5. Объявите в программе функцию, которая первым параметром принимает строку, а второй формальный параметр tag  с начальным значением в виде строки "h1" определяет тег, в который должна заключаться первая переданная строка. Например, мы передаем строку "Hello Python" и заключаем в тег "h1". Функция должна вернуть строку (без кавычек):
#"<h1>Hello Python</h1>"
#То есть, сначала открывается тег <h1>, а в конце строки - закрывается </h1>. И так для любых указанных тегов.
#После объявления функции далее в программе прочитайте из входного потока строку и дважды вызовите функцию (с выводом результата ее работы на экран):
#    первый раз только со строкой;
#    второй раз со строкой и именованным аргументом tag со значением 'div'.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.4.5
#Sample Input:
#Работаем с функциями
#Sample Output:
#<h1>Работаем с функциями</h1>
#<div>Работаем с функциями</div>



# put your python code here
def get_hypertext(st, tag = "h1"):
    return f"<{tag}>{st}</{tag}>"


lst_in = input()
print(get_hypertext(lst_in))
print(get_hypertext(lst_in, "div"))