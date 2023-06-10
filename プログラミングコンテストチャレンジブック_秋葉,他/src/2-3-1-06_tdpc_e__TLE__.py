# https://atcoder.jp/contests/tdpc/tasks/tdpc_number
# PythonだとTLE, PyPyだと通った。
# 自力はギブアップ。こちらのページを参照しました。
#   https://kanpurin.hatenablog.com/entry/2022/12/16/014741
#   https://nizi-24.hatenablog.com/entry/2021/08/08/163905
# 
# 
# DP[i][j][k] = 個数
#    i : i桁目まできめて。
#    j : Nより小さいと確定しているかの未満フラグ
#    k : i桁目までの数の和の%D
# 
# Nの上の桁から、その数(そのあとの遷移で大小関係が未定)、それ未満の数(そのあとの遷移で必ず小さくなる)で、遷移していく。
# DP[0][0][0] = 1 
# 
# DP[i+1][0][(k+n)%D] += dp[i][0][k]  where n はNの上からi+1桁目      
# 
# DP[i+1][1][(k+n)%D] += dp[i][0][k]  where n はNの上からi+1桁目より小さい値 (前者が3だったら、2,1,0)
# DP[i+1][1][(k+n)%D] += dp[i][1][k]  where n は0-9
# 
# イメージ図はこんな感じ
# 211
# ***
#   2**
#        21*
#        20*
#   
#   1**  
#        1[0-9]*
#   0**
#        0[0-9]*

# DP[Nの桁数][0][0] + dp[Nの桁数][1][0] - 1

# N以下の正整数であって、10進表記の各桁の数の和がDの倍数であるものの個数
D = int(input()) 
N = input()

DP = [[[0 for _ in range(D)] for _ in range(2)] for _ in range(len(N)+1)]
# import pprint
# pprint.pprint(DP)
# print(DP[0][0][0])
MOD = 10**9+7

DP[0][0][0] += 1
for i in range(len(N)):
    for k in range(D):
        # print(DP)
        for n in range(10):
            if n == int(N[i]):
                DP[i+1][0][(k+n)%D] += DP[i][0][k]
                DP[i+1][0][(k+n)%D] %= MOD
            elif n < int(N[i]):
                DP[i+1][1][(k+n)%D] += DP[i][0][k]

            DP[i+1][1][(k+n)%D] += DP[i][1][k]
            DP[i+1][1][(k+n)%D] %= MOD
            
# import pprint
# pprint.pprint(DP)  
print((DP[-1][-1][0]-1)%MOD)