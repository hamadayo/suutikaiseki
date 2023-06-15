import matplotlib
import matplotlib.pyplot as plot

from math import * #sin関数

#描画
def Draw(xs,xe,px,py,lx,ly):
    fig = plot.figure() #図
    graph = fig.add_subplot() #グラフを配置
    graph.set_xlim(xs,xe) #描画範囲（x軸）

    graph.plot(lx,ly) #線を描画
    graph.scatter(px,py,s=30,c="red") #点を描画

    plot.show() #表示

#ラグランジュ補完関数
def Lagrange(N,px,py,x):
    y = 0.0
    for j in range(N):
        Lj = 1.0
        for i in range(N):
            if i != j:
                Lj = Lj*(x-px[i])/(px[j]-px[i])
        y += py[j]*Lj
    return y

#実行
N = 7 #点数
px = []; py = [] #座標
for i in range(N):
    px += [0.5+i]
    py += [sin(0.5+i)]

M = 50 #x方向分割数
Lx = []; Ly = [] #曲線の座標

for i in range(0,M+1):
    x = i/M*N #注)0 < x < N
    y = Lagrange(N,px,py,x)
    Lx += [x]; Ly += [y]

Draw(0.0,float(N),px,py,Lx,Ly) #描画

# input("[Enter]キーを押して終了") #コメントアウト
