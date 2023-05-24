#学籍番号:1213033118
#氏　　名:浜田義正
#内　　容:について

from math import*
import matplotlib
import matplotlib.pyplot as plot

def Draw(x,y):
    fig = plot.figure()
    graph = fig.add.pyplot()
    graph.plot(x,y)
    graph.scatter(x,y,s=30,c="red")
    plot.show

#初期化
a = float(input("a="))
x=a
px=[]
py=[]
eps=1.0e-6
x_old=x

#反復
#for x in range(5)
while True:
    x=x/2 + a/(x+2)
    i = i + 1
    print("{0:2d} {1:.15f}")
