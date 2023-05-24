#学籍番号:1213033118
#氏　　名:浜田義正
#内　　容:収束判定値εによって終了するヤコビ法のプログラムについて


#経過表示
def Progress(k,x):
    print(k,end='')
    for val in x:
        print(' {:.8f}'.format(val), end='')
    print('')

#ヤコビ法
def Jacobi(N,A,b,eps):
    x = [0]*N #未知数ベクトル
    x_new = [0]*N #途中計算用
    a = 0

    Progress(0,x) #経過表示
    while True:
        sum = 0
        error = 0
        a += 1
        for i in range(N):
            total = 0
            for j in range(N):
                if i != j:
                    total += A[i][j]*x[j]
            x_new[i] = (b[i]-total)/A[i][i]
            sum += abs(x_new[i])
            error += abs(x_new[i] - x[i])
        
        Progress(a,x_new) #経過表示

        if error < eps * sum:
           break

        for i in range(N):
            x[i] = x_new[i] #更新
            
        #Progress(a,x)

N = 2 #未知数の個数
A = [[5,4],[2,3]] #係数行列
b = [13,8] #右辺ベクトル
eps = 1.0e-8

x = Jacobi(N,A,b,eps)

input("[Enter]キーを押して終了")