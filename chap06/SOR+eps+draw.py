#学籍番号:1213033118
#氏　　名:浜田義正
#内　　容:#内　　容:収束判定値εによって終了するSOR法のプログラムの横軸をx1,縦軸をx2とした描画と,横軸を繰り返しステップ,縦時期をx1,x2とした描画について

import matplotlib
import matplotlib.pyplot as plot

#描画
def Draw(x,y):
    fig=plot.figure()
    graph=fig.add_subplot()
    graph.plot(x,y)
    plot.xlabel('x1')
    plot.ylabel('x2')
    graph.scatter(x,y,s=30,c="red")
    plot.show()

#描画
def Draw2(x1,x2,a):
    fig=plot.figure()
    graph=fig.add_subplot()
    graph.plot(a,x1)
    graph.plot(a,x2)
    plot.xlabel('repeat step')
    plot.ylabel('x1,x2')
    graph.scatter(a,x1,s=30,c="red")
    graph.scatter(a,x2,s=30,c="green")
    plot.show()

#経過表示
def Progress(k,x):
    print(k,end='')
    for val in x:
        print(' {:.8f}'.format(val), end='')
    print('')

#SOR法
def SOR(N,A,b,omega,eps):
    x = [0]*N #未知数ベクトル
    x_new = [0]*N #途中計算用
    a = 0

    Progress(0,x) #経過表示
    while True:
      a += 1
      sum = 0
      error = 0
      for i in range(N):
          total = 0
          for j in range(N):
              if i != j:
                total += A[i][j]*x[j]
          x_new[i] = omega*(b[i]-total)/A[i][i] + (1-omega)*x[i]
          if i % 2 == 0:
              x1.append(x_new[i])
          else:
              x2.append(x_new[i])

          sum += abs(x_new[i])
          error += abs(x_new[i] - x[i])
          x[i] = x_new[i]
        
      Progress(a,x) #経過表示
      c.append(a)
      if error < eps*sum:
         break

N = 2 #未知数の個数
A = [[5,4],[2,3]] #係数行列
b = [13,8] #右辺ベクトル
omega = 1.2 #加速係数
eps = 1.0e-4
x1 = [0]
x2 = [0]
c = [0]

x = SOR(N,A,b,omega,eps)
Draw2(x1,x2,c)
Draw(x1,x2)

input("[Enter]キーを押して終了")