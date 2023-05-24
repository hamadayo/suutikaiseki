#学籍番号:1213033118
#氏　　名:浜田義正
#内　　容:収束判定値εによって終了するSOR法のプログラムについて

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
          sum += abs(x_new[i])
          error += abs(x_new[i] - x[i])
          x[i] = x_new[i]
        
      Progress(a,x) #経過表示
      if error < eps*sum:
         break

N = 2 #未知数の個数
A = [[5,4],[2,3]] #係数行列
b = [13,8] #右辺ベクトル
omega = 1.2 #加速係数
eps = 1.0e-8

x = SOR(N,A,b,omega,eps)

input("[Enter]キーを押して終了")