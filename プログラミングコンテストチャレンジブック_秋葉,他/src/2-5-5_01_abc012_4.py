# https://atcoder.jp/contests/abc012/tasks/abc012_4

N, M = map(int, input().split())
d = [[float('inf') if i!=j else 0 for j in range(N)] for i in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    d[a-1][b-1] = t
    d[b-1][a-1] = t

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

ans = min(map(lambda ele: max(ele), d))
print(ans)
# ans = ans.index(min(ans))
# print(ans+1)