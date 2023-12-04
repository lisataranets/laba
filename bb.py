import random
from random import randint
random_list = []
while True:
    try:
        M = int(input("Укажите M количество строк в списке: "))
        if M > 0 :
            break
        else:
            print("Значение должно быть больше 0")
    except ValueError:
        print("Некорректный ввод.Нужно целое число.")
while True:
    try:
        N = int(input("Укажите число N элементов в списке: "))
        if N > 0 :
            break
        else:
            print("Значение должно быть больше 0")
    except ValueError:
        print("Некорректный ввод. Нужно целое число.")
A = [0] * N
for i in range(N):
    A[i] = [0] * M

for i in range(M):
    for o in range(N):
        A[o][i]= (o+1)*10
print(A)