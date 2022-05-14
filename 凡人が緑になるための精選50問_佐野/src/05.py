#https://atcoder.jp/contests/abc190/tasks/abc190_b

N, S, D = map(int, input().split())

res = False
for i in range(N):
    x, y = map(int, input().split())

    if x >= S or y <= D:
        # not damage
        pass
    else:
        # damage
        res = True
        break

if res:
    print('Yes')
else:
    print('No')