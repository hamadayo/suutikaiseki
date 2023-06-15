#学籍番号:1213033118
#氏　　名:浜田義正
#内　　容:Lagrange+を使用した図3-6の曲線について

import matplotlib
import matplotlib.pyplot as plot
from math import*

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
N = 11#点数
px = [-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1] #x座標
py = []
for x in px:
    y = 1/(1+25*x*x)
    py.append(y)

M = 10 #
Lx = []; Ly = [] #x方向分割数

for i in range(-M,M+1):
    x = i/M #-1.0 < x < 1.0
    y = Lagrange(N,px,py,x)
    Lx += [x]; Ly += [y]



Draw(-1.0,1.0,px,py,Lx,Ly) #描画

#input("[Enter]キーを押して終了")　#コメントアウト