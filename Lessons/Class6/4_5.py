#Подвиг 6. В функцию из предыдущего подвига 5 добавьте в конец еще один третий формальный параметр up с начальным булевым значением True. Если параметр up равен True, то тег, указанный в формальном параметре tag, следует записывать заглавными буквами, а иначе малыми.
#После объявления функции далее в программе прочитайте из входного потока строку и дважды вызовите функцию (с выводом результата ее работы на экран):
#    первый раз со строкой и именованным аргументом tag со значением 'div';
#    второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.4.6
#Sample Input:
#Python is the best!
#Sample Output:
#<DIV>Python is the best!</DIV>
#<div>Python is the best!</div>


# put your python code here
def get_hypertext(st, tag = "h1", up = True):
    return f"<{tag.upper()}>{st}</{tag.upper()}>" if up else  f"<{tag}>{st}</{tag}>"


lst_in = input()
print(get_hypertext(lst_in, "div"))
print(get_hypertext(lst_in, "div", False))