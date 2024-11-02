# https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1
# 
# ある位相での最大の長さを記録していって，となりあった同士が一番大きいものを選べばよい?
# となり合う二つではなくて，隣合う三つの長さの最大値

N = int(input())
S = [*map(int, input().split())]

candid = []
tmp = 1
for i in range(N):
    if i == N-1:
        candid.append(tmp)
        break

    if S[i] == S[i+1]:
        candid.append(tmp)
        tmp = 1
    else:
        tmp += 1

if len(candid) < 3:
    print(sum(candid))
    exit(0)

ans = 0
for i in range(len(candid)-2):
    ans = max(ans, sum(candid[i:i+3]))

