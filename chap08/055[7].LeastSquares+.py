import matplotlib
import matplotlib.pyplot as plot

#描画
def Draw(px,py,a,b):
    fig = plot.figure() #図
    graph = fig.add_subplot() #グラフを配置
    xs = min(px); xe = max(px)
    graph.set_xlim(xs,xe) #描画範囲（x軸）
    lx = [xs, xe] # 始点、終点(x座標)
    ly = [a[0]*xs+b, a*xe+b] # 始点、終点(y座標)
    graph.plot(lx,ly) #線を描画
    graph.scatter(px,py,s=30,c="red") #点を描画
    plot.show() #表示

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

#関数
def f1(x):
    return x*x
def f2(x):
    return x
def f3(x):
    return x

#最小２乗法 (y=Ax^2+Bx+C)
def LeastSquares(N,x,y):
    p11 = 0.0; p12 = 0.0; p13 = 0.0
    p21 = 0.0; p22 = 0.0; p23 = 0.0
    p31 = 0.0; p32 = 0.0; p33 = 0.0
    for j in range(N):
        xj = x[j]
        p11 += f1(xj)*f1(xj); p12 += f1(xj)*f2(xj); p13 += f1(xj)*f3(xj); 
        p21 += f2(xj)*f1(xj); p22 += f2(xj)*f2(xj); p23 += f2(xj)*f3(xj); 
        p31 += f3(xj)*f1(xj); p32 += f3(xj)*f2(xj); p33 += f3(xj)*f3(xj); 
    pki = [[p11,p12,p13],[p21,p22,p23],[p31,p32,p33]]
    q1 = 0.0; q2 = 0.0; q3 = 0.0
    for j in range(N):
        xj = x[j]; yj = y[j]
        q1 += yj*f1(xj); q2 += yj*f2(xj); q3 += yj*f3(xj)
    qk = [q1,q2,q3]

    return Gauss(3,pki,qk)

#実行
N = 5 #点数
x = [0.0, 0.5, 1.0, 1.5, 2.0] #x座標
y = [-0.45, 0.20, 0.53, 0.28, -0.62] #y座標

ABC = LeastSquares(N,x,y)
print('A =',ABC[0],', B =',ABC[1],' C =',ABC[2])

M = 20
Draw(x,y,ABC,M) #描画

#input("[Enter]キーを押して終了") #コメントアウト
