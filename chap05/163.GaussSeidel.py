#経過表示
def Progress(k,x):
    print(k,end='')
    for val in x:
        print(' {:.8f}'.format(val), end='')
    print('')

#ガウスーザイデル法
def GaussSeidel(N,A,b,M):
    x = [0]*N #未知数ベクトル

    Progress(0,x) #経過表示
    for k in range(1,M+1): #反復ループ
      for i in range(N):
          total = 0
          for j in range(N):
              if i != j:
                  total += A[i][j]*x[j]
          x[i] = (b[i]-total)/A[i][i]
      Progress(k,x) #経過表示
      
    return x

N = 2 #未知数の個数
A = [[5,4],[2,3]] #係数行列
b = [13,8] #右辺ベクトル
M = 41 #反転回数

x = GaussSeidel(N,A,b,M)

input("[Enter]キーを押して終了")