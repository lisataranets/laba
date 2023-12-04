import random
from random import randint
while True:
    try:
        n = int(input("Укажите количество строк в списке: "))
        if n > 0 :
            break
        else:
            print("Значение должно быть больше 0")
    except ValueError:
        print("Некорректный ввод. Нужно целое число.")
while True:
    try:
        k = int(input("Укажите количество элементов в строке: "))
        if k > 0 :
            break
        else:
            print("Значение должно быть больше 0")
    except ValueError:
        print("Некорректный ввод. Нужно целое число.")

A = [0] * k
for j in range(k):
    A[j] = [0] * n
for i in range(n):
    for o in range(k):
        A[i][o]= random.randint(-100,100)
print(A)

spisok_summ=[]
summ=0
for o in A:
    for i in o:
        if i%2==0 and i<0:
            summ+=i
    spisok_summ.append(summ)
    summ=0
print(spisok_summ)

for i in range(len(spisok_summ)):
    for g in range(i+1,len(spisok_summ)):
        if spisok_summ[i]>spisok_summ[g]:
            spisok_summ[i],spisok_summ[g] = spisok_summ[g],spisok_summ[i]
print(spisok_summ)