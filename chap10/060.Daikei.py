from math import*

def f(x):
    return exp(x)

def Daikei(N,a,b): #台形側
    h = (b-a)/N
    T = h*(f(a)+f(b))/2
    for j in range(1,N):
      x = a+j*h
      T += h*f(x)

    return T

# 実行
N = 1
a = 0
b = 1

I = Daikei(N,a,b)
print("{0:4d} {1:.8f}".format(N,I)) 
input("[Enter]キーを押して終了")
