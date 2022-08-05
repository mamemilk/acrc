# https://atcoder.jp/contests/abc158/tasks/abc158_d
# TLEが解決できずで，カンニング

from collections import deque

S = input()
Q = int(input())

S_dq = deque()
for s in S:
    S_dq.append(s)

is_flip = False

for n in range(Q):
    pre = input().split()
    if len(pre) == 1:
        t = int(pre[0])
    else:
        t = int(pre[0])
        f = int(pre[1])
        c = pre[2]

    if t == 1:
        is_flip ^= True
    elif t == 2:
        if f == 1: # 先頭
            if is_flip:
                # S = S + c
                S_dq.append(c)
            else:
                #S = c + S
                S_dq.appendleft(c)
        elif f == 2: # 末尾
            if is_flip:
                #S = c + S
                S_dq.appendleft(c)
            else:
                #S = S + c
                S_dq.append(c)

res = "".join(S_dq)
if is_flip:
    print(res[::-1])
else:
    print(res)