# https://atcoder.jp/contests/abc091/tasks/abc091_b
# 
# 


rk = {}

N = int(input())
for _ in range(N):
    s = input()
    if s in work.keys():
        work[s] = work[s] + 1
    else:
        work[s] = 1

M = int(input())
for _ in range(M):
    t = input()
    if t in work.keys():
        work[t] = work[t] - 1

m = max(work.values())
if m < 0:
    print(0)
else:
    print(m)