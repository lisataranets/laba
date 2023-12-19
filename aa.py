def SortLnk(a,b,c):
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    if a>c:
        a,c=c,a
    if a > b:
        a, b = b, a
    return a,b,c
while True:
    try:
        A_1= float(input("Укажите число A_1 для первого набора: "))
        B_1 = float(input("Укажите число B_1 для первого набора: "))
        C_1 = float(input("Укажите число C_1 для первого набора: "))
        break
    except ValueError:
        print("Некорректный ввод. Нужен набор из чисел. Повторите ввод")
print(SortLnk(A_1,B_1,C_1))
while True:
    try:
        A_2= float(input("Укажите число A_2 для второго набора: "))
        B_2 = float(input("Укажите число B_2 для второго набора: "))
        C_2 = float(input("Укажите число C_2 для второго набора: "))
        break
    except ValueError:
        print("Некорректный ввод. Нужен набор из чисел. Повторите ввод")
print(SortLnk(A_2,B_2,C_2))