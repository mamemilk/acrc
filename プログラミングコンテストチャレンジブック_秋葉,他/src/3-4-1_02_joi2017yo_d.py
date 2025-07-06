# https://atcoder.jp/contests/joi2017yo/tasks/joi2017yo_d
# 
# https://starpentagon.net/analytics/plushtoys/
# https://scrapbox.io/jikky/JOI_2017_%E4%BA%88%E9%81%B8_D_-_%E3%81%AC%E3%81%84%E3%81%90%E3%82%8B%E3%81%BF%E3%81%AE%E6%95%B4%E7%90%86_(%E9%9B%A3%E6%98%93%E5%BA%A67)



N, M = map(int, input().split())

A = [int(input()) - 1 for _ in range(N)]

# acc[i][j] 種類iのぬいぐるみが区間 [0, j)にある個数
acc = [[0]*(N+1) for _ in range(M)] 
for i in range(M):
    for j in range(N):
        acc[i][j+1] = acc[i][j] + (A[j] == i)


dp = [N for _ in range(1<<M)]
dp[0] = 0

for bit in range(1<<M):
    left = 0
    for i in range(M):
        if bit & (1<<i):
            left += acc[i][N]

    for i in range(M):
        if bit & (1<<i): continue
        right = left + acc[i][N]
        cost = (right - left) - (acc[i][right] - acc[i][left])
        dp[bit | (1<<i)] = min(dp[bit | (1<<i)], dp[bit] + cost)

print(dp[-1])