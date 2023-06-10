# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_E&lang=jp
# 
# reference : https://qiita.com/sinchir0/items/02697cae7f960356eaba
# 

s1 = input()
s2 = input()

DP = [[float('inf') for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
for j in range(len(s1)+1):
    DP[0][j] = j
for i in range(len(s2)+1):
    DP[i][j] = i


for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        DP[i][j] = min(DP[i][j-1] + 1, 
                       DP[i-1][j] + 1,
                       DP[i-1][j-1] if s1[j-1] == s2[i-1] else DP[i-1][j-1] + 1)

print(DP[-1][-1])