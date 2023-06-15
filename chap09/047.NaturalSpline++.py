import matplotlib
import matplotlib.pyplot as plot

from math import * #sin関数

#Gaussの消去法
def Gauss(N,A,y):
    x = [0]*N #未知数ベクトル
    #前進消去
    for k in range(N-1):
        m = 0 #最大値
        for i in range(k,N):
            if m < abs(A[i][k]):
                m = abs(A[i][k])
                l = i
            if l != k:
                for n in range(k,N):
                    A[k][n],A[l][n] = A[l][n],A[k][n]
                y[k],y[l] = y[l],y[k]
                for i in range(k+1,N):
                    alpha = A[i][k]/A[k][k]
                    for j in range(k+1,N):
                        A[i][j] -= alpha*A[k][j]
                    y[i] -= alpha*y[k]

    #後退代入
    x[N-1] = y[N-1]/A[N-1][N-1]

    for i in range(N-2,-1-1):
        s = 0 #合計
        for k in range(i+1,N):
            s += A[i][k]*x[k]
        x[i] = (y[i] - s)/A[i][i]

    return x

# [xs,xe] 間をndiv分割したときにi番目となる点のx座標(0=<i=<ndiv)
def xi(i,xs,xe,ndiv):
    return xs*(ndiv-i)/ndiv+xe*i/ndiv

#描画
def Draw(px,py,a,b,c,d):
    fig = plot.figure() #図
    graph = fig.add_subplot() #グラフを配置
    N = len(a) #リストaの要素数
    graph.set_xlim(px[0],px[N]) #描画範囲（x軸）

    #スプライン曲線
    for j in range(len(a)):
        xj = px[j]; xk = px[j+1] #区間の両端の座標
        qx = []; qy = [] #座標
        M = 10 # 区間をM分割
        for i in range(M+1):
            x = xi(i,xj,xk,M)
            y = a[j]*(x-xj)**3+b[j]*(x-xj)**2+c[j]*(x-xj)+d[j]
            qx += [x]
            qy += [y]
            
        graph.plot(qx,qy) #線を描画
    graph.scatter(px,py,s=30,c="red") #点を描画

    plot.show() #表示

#自然スプライン
def NaturalSpline(N,px,py):
    h = [0]*N
    for j in range(N):
        h[j] = px[j+1]-px[j]
    v = [0]*N
    for j in range(N):
        v[j] = 6*((py[j+1]-py[j])/h[j]-(py[j]-py[j-1])/h[j-1])
    #連立方程式の作成
    A = [] #係数行列
    for i in range(N-1):
        A += [[0]*(N-1)]
    for i in range(N-1):
        A[i][i] = 2*(h[i]+h[i+1]) #対角成分
    for i in range(N-2):
        A[i][i+1] = h[i+1] #対角周辺
        A[i+1][i] = h[i] #対角周辺
    y = [0]*(N-1) #右辺ベクトル
    for i in range(N-1):
        y[i] = v[i+1]

    x = Gauss(N-1,A,y) #p.47(3.32)式

    u = [0] + x + [0] #両端の境界条件
    b = [0]*N
    for j in range(N):
        b[j] = u[j]/2 # (3.20)式
    a = [0]*N
    for j in range(N):
        a[j] = (u[j+1]-u[j])/(6*(px[j+1]-px[j])) # (3.22)式
    d = [0]*N
    for j in range(N):
        d[j] = py[j] #(3.24)式
    c = [0]*N
    for j in range(N):
        c[j] = (py[j+1]-py[j])/(px[j+1]-px[j])-(px[j+1]-px[j])*(2*u[j]+u[j+1])/6 #(3.25)式

    return a,b,c,d

# 関数
def f(x):
    return 1/(1+25*x**2)
# 範囲[xs,xe]
xs = -1.0; xe = 1.0

#実行
N = 10 #点数
px = [] #x座標
py = [] #y座標
for i in range(N+1):
    x= xi(i,xs,xe,N)
    y = f(x)
    px += [x]
    py += [y]

a,b,c,d = NaturalSpline(N,px,py)

Draw(px,py,a,b,c,d) #描画

#input("[Enter]キーを押して終了")　#コメントアウト