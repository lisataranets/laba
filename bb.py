from random import randint
random_list = []
while True:
    try:
        n = int(input("Укажите количество элементов в списке: "))
        if n > 0 :
            break
        else:
            print("Значение n должно быть больше 0")
    except ValueError:
        print("Некорректный ввод.Нужно целое число.")
for i in range(n):
    random_list.append(randint(1, 100))
while True:
    try:
        C = int(input("Укажите число C: "))
        if C > 0 :
            break
        else:
            print("Значение C должно быть больше 0")
    except ValueError:
        print("Некорректный ввод. Нужно целое число.")
count = 0
for element in random_list:
    if element < C:
        count += 1
print(random_list)
print("Количество элементов списка меньше C:", count)
