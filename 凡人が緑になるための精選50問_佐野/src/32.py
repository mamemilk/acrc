 # https://atcoder.jp/contests/abc190/tasks/abc190_d
 # 以下式でやる．演算時間超過すると思いきや，最長で240msecだった．
 # 
 # (a + a + n - 1) * n / 2
 # (2an + n^2 - n) / 2 = N 
 # 2an + n^2 - n = 2N 
 # 2a + n - 1 = 2N / n     => nは，2Nの約数
 # 2a = 2N/n - n + 1       
 #  a = (2N/n - n + 1) / 2 => 右辺が2で割り切れれば，aは存在
 #  

import math

N = int(input())

ans = 0

for i in range(1, int(math.sqrt(2*N) + 1)):
    if (2*N)%i==0:
        pass
    else:
        continue

    if i**2 == 2*N:
        n = i
        if ((2*N)//n - n + 1)%2 == 0:
            ans += 1
    else:
        n = i
        if ((2*N)//n - n + 1)%2 == 0:
            ans += 1
        
        n = (2*N)//i
        if ((2*N)//n - n + 1)%2 == 0:
            ans += 1
        
print(ans)

    