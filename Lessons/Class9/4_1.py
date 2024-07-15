#Подвиг 5. Пользователь может ввести с клавиатуры следующие команды в виде строки:
#top или Top или TOP
#bottom или Bottom или BOTTOM
#right или Right или RIGHT
#left или Left или LEFT
#cmd = input() 
#С помощью оператора match/case необходимо определить тип команды cmd и при совпадении вывести на экран сообщение в формате:
#Команда <название команды малыми буквами>
#Например, при вводе Top, должны на выходе получить:
#Команда top
#И так для всех четырех команд. Если тип команды не определен, то вывести строку:
#Неверная команда
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.4.5
#Sample Input:
#BOTTOM
#Sample Output:
#Команда bottom



cmd = input()
match cmd:
    case "top" | "Top" | "TOP":
        print("Команда top")
    case "bottom" | "Bottom" | "BOTTOM":
        print("Команда bottom")
    case "right" | "Right" | "RIGHT":
        print("Команда right")
    case "left" | "Left" | "LEFT":
        print("Команда left")
    case _:
        print("Неверная команда")