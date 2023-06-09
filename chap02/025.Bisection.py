from math import*

#関数
def f(x):
    return exp(-x)-x*x

#初期値の設定（ステップ（１））
a = 1
b = 0
eps = 1.0e-6
n = 0

#反復（ステップ（２））
while True:
    c = (a+b)/2
    n = n + 1
    print("{0:2d} {1:.7f}".format(n,c))

    if abs(a-b)/2 < eps:
        break #ステップ（3）に移る
    fc = f(c)

    if fc > 0:
        b = c
    elif fc < 0:
        a = c
    else:
        break #ステップ（3）に移る
    
#終了(ステップ(3))
print("\nc=",c)
input("\n[Enter]キーを押して終了")