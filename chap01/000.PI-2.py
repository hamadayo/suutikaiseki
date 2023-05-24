#学籍番号:1213033118
#氏　　名:浜田義正
#内　　容:について

from math import*

def Renew(a,b,t,p):
    new_a = (a+b)/2
    new_b = sqrt(a*b)
    new_t = t-p*(a-new_a)**2
    new_p = 2*p
    return new_a,new_b,new_t,new_p

#初期化
a = 1
b = 1/sqrt(2)
t = 1/4
p = 1

#反復
for i in range(5):
    a,b,t,p = Renew(a,b,t,p)
    print("{0:2d} {1:.15f}".format(i+1,((a+b)**2)/(4*t))) #2dは2桁の整数表示　　.15fは小数点以下15桁表示

    #入力待ち
    input("[Enter]キーを押して終了")