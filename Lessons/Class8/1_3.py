#Подвиг 3. На вход программе поступают два целых числа a и b (a < b), записанные в одну строчку через пробел. Определите генератор, который бы выдавал модули целых чисел из диапазона [a; b] (включительно). 
#В цикле выведите первые пять значений этого генератора. Каждое значение с новой строки. (Гарантируется, что пять значений имеются).
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.1.3
#Sample Input:
#-3 3
#Sample Output:
#3
#2
#1
#0
#1


# put your python code here
a, b = map(int, input().split())
gen = (abs(x) for x in range(a, b + 1))
for i in range(5):
    print(next(gen))