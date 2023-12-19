import random
X=[random.randint(-100,100) for i in range(15)]
Y=[random.randint(-100,100) for i in range(15)]
print(X)
print(Y)
def f(n):
    a=n[0]
    for i in range(1,len(n)):
        if n[i]<a:
            a=n[i]
    return a
z=(f(X)+f(Y))/f(X)*f(Y)
print(z)
