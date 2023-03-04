# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=jp
#  longest common subsequencen 
# net de sirabeta. koreha hassou dekin

N = int(input())

def lcs(x, y):
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for xi in range(len(x)):
        for yi in range(len(y)):
            if x[xi] == y[yi]:
                dp[xi+1][yi+1] = dp[xi][yi] + 1
            else:
                dp[xi+1][yi+1] = max(dp[xi][yi+1], dp[xi+1][yi])

    return dp[-1][-1]

ans = []
for _ in range(N):
    x = input()
    y = input()

    ans.append(lcs(x,y))

for a in ans:
    print(a)
    
