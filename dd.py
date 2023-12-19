import random
def PowerN(X,N):
    if N==0:
        return 1
    elif N>0 and N%2==0:
        return PowerN(X,N//2)**2
    elif N>0 and N%2!=0:
        return X*PowerN(X,N-1)
    else:
        return 1/PowerN(X,-N)
while True:
    try:
        X = float(input("Укажите число X "))
        break
    except ValueError:
        print("Некорректный ввод. Нужно число")
N_n=[]
for i in range(10):
    n=(input("Укажите пять значений N"))
    try:
        nc=int(n)
        N_n.append(nc)
    except ValueError:
        print("Некорректный ввод. Нужно целое число")
    if len(N_n)==5:
        break
print(N_n)
for N in N_n:
    print(PowerN(X,N))