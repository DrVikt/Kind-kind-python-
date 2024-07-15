#Подвиг 4. Вводятся данные по книге в виде строки через запятую в формате (некоторые значения могут отсутствовать):
#id, автор, название, цена, год издания
#с помощью команд:
#t = (int, str, str, float, int)
#book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
#Например, при вводе:
#"1, Балакирев С.М., Python, 2100, 2023"
#получим список:
#book = [1, 'Балакирев С.М.', 'Python', 2100.0, 2023]
#А при вводе:
#"1, Балакирев С.М., Python"
#список:
#book = [1, 'Балакирев С.М.', 'Python']
#И так далее.
#С помощью оператора match/case необходимо определить шаблоны для выделения следующей информации:
#автор, название
#автор, название, цена
#автор, название, год издания
#автор, название, цена, год издания
#Первый шаблон срабатывает, если есть только автор и название; второй, если появляется еще и цена; третий, если есть автор, название, год издания, но нет цены; последний, если имеются все данные.
#При срабатывании шаблона вывести на экран строку "Yes". Если ни один из шаблонов не сработал, то вывести строку "No".
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.5.4
#Sample Input:
#1, Балакирев С.М., Python, 2100.0, 2023
#Sample Output:
#Yes



t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
match book:
    case (_, str()  as author, str()  as name): print("Yes")
    case (_, str()  as author, str() as name, float() as price): print("Yes")
    case (_, str() as author, str() as name, int() as year): print("Yes")
    case (_, str() as author, str() as name, float() as price, int() as year): print("Yes")
    case book: print("No") 