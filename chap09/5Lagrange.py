#学籍番号:1213033118
#氏　　名:浜田義正
#内　　容:Lagrange+を使用した4区間と8区間の波形の近似曲線について

import matplotlib
import matplotlib.pyplot as plot

#描画
def Draw(px,py,lx,ly):
    N = len(px) #len(px):pxの要素数
    fig = plot.figure() #図
    graph = fig.add_subplot() #グラフを配置
    graph.set_xlim(px[0],px[N-1]) #描画範囲（x軸）

    graph.plot(lx,ly) #線を描画
    graph.scatter(px,py,s=30,c="red") #点を描画

    plot.show() #表示

#ラグランジュ補完関数
def Lagrange(px,py,x):
    N = len(px)
    y = 0.0
    for j in range(N):
        Lj = 1.0
        for i in range(N):
            if i != j:
                Lj = Lj*(x-px[i])/(px[j]-px[i])
        y += py[j]*Lj
    return y
    
# 関数
def f(x):
    return 1/(1+25*x**2)

# [xs,xe] 間をndiv分割したときにi番目となる点のx座標(0=<i=<ndiv)
def xi(i,xs,xe,ndiv):
    return xs*(ndiv-i)/ndiv+xe*i/ndiv
# 範囲[xs,xe]
xs = -1.0; xe = 1.0

#サンプル点
px = [-1,-0.5,0,0.5,1]; py = [0,1,0,-1,0]
px1 = [-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1]; py1 = [0,0.5,1,0.5,0,-0.5,-1,-0.5,0]

#曲線を構成する点群
M = 200 #点数
Lx = []; Ly = [] #曲線上の点
Lx1 = []; Ly1 = [] #曲線上の点

for i in range(M+1):
    x = xi(i,xs,xe,M)
    y = Lagrange(px,py,x)
    Lx += [x]; Ly += [y]

for i in range(M+1):
    x1 = xi(i,xs,xe,M)
    y1 = Lagrange(px1,py1,x1)
    Lx1 += [x1]; Ly1 += [y1]


Draw(px,py,Lx,Ly) #描画
Draw(px1,py1,Lx1,Ly1) #描画


#input("[Enter]キーを押して終了")　#コメントアウト