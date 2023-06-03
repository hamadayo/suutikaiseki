#ラグランジュ補完関数
def Lagrange(N,px,py,x):
    y = 0.0
    for j in range(N):
        Lj = 1.0
        for i in range(N):
            if i != j:
                Lj = Lj*(x-px[i])/(px[j]-px[i])
        y = y + py[j]*Lj
    return y

#メイン
N = 3                 #点数
px = [0.2, 0.6, 0.8]  #x座標
py = [0.3, 0.8, 0.4]  #y座標
M = 10                #求めたい曲線上の点の数

for i in range(0, M+1):
    x = i/M     #0.0 < x < 1.0
    y = Lagrange(N,px,py,x)
    print('{0:.3f} {1:.3f}'.format(x,y))

input("[Enter]キーを押して終了")