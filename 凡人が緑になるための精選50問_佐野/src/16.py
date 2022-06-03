# https://atcoder.jp/contests/abc183/tasks/abc183_c

import itertools

N, K = map(int, input().split())

Tij = []
for n in range(N):
    row = list(map(int, input().split()))
    Tij.append(row)

res = 0
for p in itertools.permutations(range(2,N+1),N-1):
    dis_sum = 0
    _prev = 1
    for _next in list(p):
        dis = Tij[_prev-1][_next-1]
        dis_sum += dis

        if dis_sum > K:
            break

        _prev = _next

    _next = 1
    dis = Tij[_prev-1][_next-1]
    dis_sum += dis

    #print(p, dis_sum)

    if dis_sum == K:
        res += 1

print(res)
    