# https://atcoder.jp/contests/abc073/tasks/abc073_d

import itertools

N, M, R = map(int, input().split())
ri = list(map(int, input().split()))

d = [[float('inf') if i!=j else 0 for j in range(N)] for i in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    d[A-1][B-1] = C
    d[B-1][A-1] = C

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

ans = float('inf')
for v in itertools.permutations(ri):
    tmp = 0
    for (index, city) in enumerate(v[:-1]):
        city_next = v[index+1]
        tmp += d[city-1][city_next-1]

    ans = min(tmp, ans)

print(ans)


# ans = ans.index(min(ans))
# print(ans+1)