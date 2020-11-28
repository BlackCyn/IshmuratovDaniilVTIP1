import math
from random import *
import doctest

def per(a=1):
    per = (a*4)
    return per
print(per(int(input('Введите длину стороны'))))

def Sq(a=1):
    Sq=a*a
    return Sq
print(Sq(int(input('Введите сторону квадрата чтобы узнать ее площадь'))))

def Sred(a,b,c):
    Sred=(a+b+c)/3
    return Sred
print('Введите 3 число через запятую')
a,b,c=map(int,input().split(','))
print('Среднее арифметическое равно', Sred(a,b,c))

def sec():
    N=int(input('Введите количество секунд, прошедших с начала дня'))
    if (N>3600):
        A=N%3600
        B=A//60
        print("количество полных минут, прошедших с начала последнего часа равно ",B)
    else:
        B=N//60
        print("количество полных минут, прошедших с начала последнего часа равно ",B)
sec()

s=input("Как вас зовут?")
print('Hello ',s)

a=int(input("Введите первое число"))
b=int(input("Введите второе число"))
c=int(input("Введите третье число"))
summ=a+b+c
print("Сумма введенных чисел равна ",summ)
Umn=a*b*c
print("Произведение введенных чисел равна ",Umn)

print("Введите показатель pH")
pH=int(input())
if(pH<7):
    print("Кислотный раствор")
else:
    print("Основной раствор")

print("Привет!\nВведи сколько ты весишь и свой рост через запятую")
a,b=map(int,input().split(','))
b=b/100
BMI=a/(b*b)
print ("Твой Индекс массы дела составляет", BMI)
if(BMI<16):
    print("Выраженный дефицит массы тела")
elif (BMI >= 16 and BMI < 18.5):
    print("Недостаточная масса тела")
elif (BMI>=18.5 and BMI < 25):
    print("Норма")
elif(BMI>=25 and BMI<30):
    print("Избыточная масса тела")
elif(BMI>=30 and BMI<35):
    print("Ожирение")
elif(BMI>=35 and BMI<40):
    print("Ожирение резкое")
elif(BMI>=40):
    print("Очень резкое ожирение")

def dva(a,b):
    if(a>b):
        print("Наибольшим из лвух чисел является число ",a);
    else:
        print("Наибольшим из лвух чисел является число ",b);
print('Введите два числа через запятую')
a,b=map(int,input().split(','))
dva(a,b)

def chet(a):
    if(a%2==0):
        print("Введенное число является четным")
    else:
        print("Введенное число является нечетным")
a=int(input("Введите число"))
chet(a)

def a(x):
    if (x**2>=-2.4 and x**2<=5.7):
        print("Результат данной функции равен ",x**2)
    else:
        print("Результат данной функции равен ",4)
x=float(input("Введите вещественное число"))
a(x)

def function55(city, minutes):
    if (city == "Екатеринбург" or city == 343):
        print(minutes * 15)
    if (city == "Омск" or city == 381):
        print(minutes * 18)
    if (city == "Воронеж" or city == 473):
        print(minutes * 13)
    if (city == "Ярославль" or city == 485):
        print(minutes * 11)
    print("Выведенное число равна стоимости разговора по телефону")
city=int(input("Введите код города из которого совершался звонок из перечисленных\n343-Екатеринбург\n381-Омск\n473-Воронеж\n485-Ярославль\n"))
minutes=int(input("Введите количество минут"))
function55(city,minutes)

def s(a,b,c):
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    if (S==0):
        print("Такого треугольника не существует")
    else:
        print("Площадь треугольника равна", S)
print('Введите три стороны треугольника через запятую, чтобы вычислить площадь')
a,b,c=map(float,input().split(','))
s(a,b,c)

def pi():
    pi= round(math.pi,2)
    print('Число пи округленное до сотых равно ',pi)
pi()

def formula(x):
    a = math.sqrt(1 - math.sin(x) ** 2)
    print("Результат выражения(1-sin^2(X) под квадратным корнем) равен ",a)
x=float(input('Введите X'))
formula(x)

def game(x):
    import random
    s=random.randint(1,10)
    print("Я загадал", s)
    if (s == x):
        print("Ты победил! ты молодец")
    else:
        print("Не повезло:( Попробуй еще раз!")
x=int(input("Попробуй угадать число, которое я загадал. напиши его"))
game(x)

def fun1(x):
    a=x**4+4**x
    print(a)
x=float(input("Введи число чтобы вычислить ответ у функции"))
fun1(x)
doctest.testmod(fun1(x))

def fun2(x):
    if (math.sin(x) >= 0.2 and math.sin(x) <= 0.9):
        print ("Результат функии равен ",math.sin(x))
    else:
        print ("Результат функии равен ",1)
x=float(input("Введите вещественное чсло Х чтобы вычислить значение функции"))
fun2(x)

print("Программа для моделирования бросания игрального кубика каждым из двух игроков")
def fun3():
    import random
    a1 = random.randint(1, 6)
    b1 = random.randint(1, 6)
    c1 = random.randint(1, 6)
    a2 = random.randint(1, 6)
    b2 = random.randint(1, 6)
    c2 = random.randint(1, 6)
    PL1 = a1 + b1 + c1
    PL2 = a2 + b2 + c2
    if (PL1 > PL2):
        print("Победил первый игрок, он набрал", PL1, "очков из максимальных 18")
    else:
        print("Победил второй игрок, он набрал", PL2, "очков из максимальных 18")
fun3()

print("\nПрограмма для нахождения буквы я в предложении (У лукоморья 123 дуб зеленый 456)")
def fun4():
    s = "У лукоморья 123 дуб зеленый 456"
    a = s.find('я')
    if (a != -1):
        print("буква 'я' есть в данном предложении")
        print("ее позиция =", a)
    else:
        print("В этом предложении нет буквы 'я'")
fun4()

print("\nПрограмма подсчета быквы У в предложении (У лукоморья 123 дуб зеленый 456)")
def fun5():
    s = "У лукоморья 123 дуб зеленый 456"
    a = s.count('у')
    b = s.count('У')
    c = a + b
    print("Буква 'y' в данном предложении встречается ", c, "раз(а)")
fun5()

print("\nПрограмма для определения состоит ли строка только из букв, ЕСЛИ нет, ТО вывести строку в верхнем регистре. (У лукоморья 123 дуб зеленый 456)")
def fun6():
    s = "У лукоморья 123 дуб зеленый 456"
    a = s.find('0')
    b = s.find('1')
    c = s.find('2')
    d = s.find('3')
    e = s.find('4')
    f = s.find('5')
    g = s.find('6')
    h = s.find('7')
    j = s.find('8')
    k = s.find('9')
    if (a != -1 or b != -1 or c != -1 or d != -1 or e != -1 or f != -1 or g != -1 or h != -1 or j != -1 or k != -1):
        print("В этой строке есть цифры")
        z = s.upper()
        print(z)
    else:
        print("В этой строке нет цифр")
fun6()

print("\nОпределить длину строки. ЕСЛИ длина строки превышает 4 символа, ТО вывести строку в нижнем регистре.(У лукоморья 123 дуб зеленый 456)")
def fun7():
    s = "У лукоморья 123 дуб зеленый 456"
    if (len(s) > 4):
        z = s.lower()
        print(z)
    else:
        print("В этой строке меньше 4 символов или 4 символа")
fun7()

print("\nЗаменить в строке первый символ на 'О'. Результат вывести на экран.(У лукоморья 123 дуб зеленый 456)")
def fun8():
    s = "У лукоморья 123 дуб зеленый 456"
    line = s.replace(s[0], 'О')
    print (line)
fun8()

def fun9(s,n):
    if(len(s)>n):
        print("Так как количество символов в предложении больше введенного числа, по условию задачи мы выведем данное предложение в верхнем регистре\n",s.upper())
    else:
        print("Так как количество символов в предложении меньше или равно введенному числу, по условию задачи мы выведем данное предложение без изменений\n",s)
s=input("Введите какое нибудь короткое предложение")
n=int(input("Введите число"))
fun9(s,n)

def fun123():
    L = [3, 6, 7, 4, -5, 4, 3, -1]
    sum = 0
    for i in L:
        sum += i
    print("\nСумма элементов списка (3, 6, 7, 4, -5, 4, 3, -1) равна ",sum)
    if(sum>2):
        print("Так как сумма элементов списка больше 2, выведеи количество элементов:",len(L))
    a=min(L)
    b=max(L)
    if((b-a)>10):
        L.sort()
        print("Так как разность максимального и минимального элемента списка больше 10, отсортируем список: ",L)
    else:
        print("Разность меньше 10")


fun123()

print("\nОпределите наличие строки «привет» в списке. ЕСЛИ такая строка в списке присутствует, ТО вывести ее на экран, повторив 10 раз.")
def fun124():
    L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
    a=0
    for i in L:
        if (i == 'привет'):
            print(i * 10)
fun124()

print("\nНесколько примеров среза")
def fun125():
    L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
    print(L[:])
    print(L[1:])
    print(L[:3])
    print(L[::2])
    print(L[::-1])
fun125()

print("\nОпределите наличие строки «привет» в списке. ЕСЛИ такая строка в списке присутствует, ТО удалить ее из списка, ИНАЧЕ добавить строку в список. Подсчитать, сколько раз в списке встречается число 4, ЕСЛИ больше одного раза, ТО очистить список.")
def fun126():
    L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
    if 'привет' in L:
        L.remove('привет')
        print(L)
    if L.count(4) > 1:
        L.clear()
        print(L)
fun126()

def fun127():
    L = ['самовар', 'весна', 'лето']
    sl = choice(L)
    n = randint(0, len(sl) - 1)
    print("\nПопробуйте угадать пропущенную букву")
    for i in range(len(sl)):
        if i == n:
            print('?', end='')
            continue
        print(sl[i], end='')

    while True:
        f = input('\nВведите букву: ')
        if f == sl[n]:
            print('Вы победили!')
            break
        else:
            print('Не угадали:( Попробуйте еще!')
fun127()

def fun128():
    x=10
    y=0
    while (x<=30):
        y=x**2+3
        x=x+2
        print (y)
print("\nНайдите все значения функции y (x) = x2 + 3 на интервале от 10 до 30 с шагом 2.")
fun128()

def fun129():
    List = [-8,8,6.0,5,'строка',-3.1]
    s=0
    for i in List:
        if(type(i)==int or type(i)==float):
            s=s+i
    print("\nСумма чисел входящих в список (-8, 8, 6.0, 5, 'строка', -3.1) равна ",s)
fun129()

def fun130():
    a = [-8, 8, 6.0, 5, 'строка', -3.1]
    if len(a) % 2 != 0:
        print('\nнечетное количество элементов в списке')
    else:
        print("\nИсходный список",a)
        print("Список, в котором первая и вторая половина поменялись местами",a[len(a) // 2:] + a[0: len(a) // 2])
fun130()

def fun131():
    import random
    print("\nПопробуй угадать число которое я загадал(от 0 до 5)")
    n = random.randint(0, 5)
    while True:
        text = input("Введите число или выход для выхода: ")
        if text == "выход":
            print("До встречи! Загадано было", n)
            break  
        elif int(text) == n:
            print("Победа")
            break
        else:
            print("Попробуйте еще раз")
fun131()

def fun132():
    n = input("\nВведите какое нибудь большое число(например 1234)")
    if all(map(str.isdigit, n)):
        a = 0
        n = list(map(int, n))
        for i in n:
            if i % 2 != 0:
                a += i ** 2
        print("Сумма квадратов нечетных цифр в числе равна ",a)
    else:
        print('Вы ввели неправильное значение')
fun132()

def fun133():
    sum = 0
    print('\n')
    while True:
        n = input("Введите число или выход для выхода: ")
        if str(n) == "выход":
            print("Сумма введенных чисел равна",sum)
            break  
        else:
            sum = sum + int(n)
            print(sum)
fun133()

def fun134(text):
    w = text.split(' ')
    l = list(map(len, w))
    return l.index(max(l)) + 1

s="Меня зовут Ишмуратов Даниил"
print("\n",s)
print("Номер первого самого длинного слова в данной строке равен",fun134(s))

def fun135():
    s = "Строка98сцифра23ми"
    print("\n",s)
    sum = 0
    count = 0
    for i in range(len(s)):
        if s[i].isdigit():
            count = count + 1
        if s[i].isalpha():
            continue
        sum = sum + int(s[i])
    print("сумма чисел", sum, ", количество чисел:", count, ',максимальное число', max(int(x) for x in s if x.isdigit()))
fun135()

def fun136():
    from random import randint
    N = 3
    M = 5
    lst = [[randint(-5, 5) for i in range(N)] for i in range(M)]
    print("Матрица 3х5 заплненная случайными числами от -5 до 5")
    for i in lst:
        print()
        for j in i:
            print(j, end=" ")
fun136()








