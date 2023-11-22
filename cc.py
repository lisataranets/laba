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
now_list=[]
for i in range(len(random_list)-1, -1, -1):
        now_list.append(random_list[i])
print("старый список:",random_list)
print("новый список:",now_list)