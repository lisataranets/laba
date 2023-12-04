while True:
    try:
        N = int(input("Укажите число N стран в словаре: "))
        if N > 0 :
            break
        else:
            print("Значение должно быть больше 0")
    except ValueError:
        print("Некорректный ввод. Нужно целое число.")
city={}
for i in range(N):
    info = input("Добавьте в словарь информацию: страна город ").split()
    for k in info[1:]:
        city[k] = info[0]
m=input('Введите название города: ')
if m in city:
    print("Этот город расположен в стране: ",city.get(m))
else:
    print(" ")