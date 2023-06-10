# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0503
# 
# キューには状態を入れる，という発想ができてなかった．
# 
# 
#    A-B, B-Cのどちらかを選んだら，
#    A<->B, B<->C, A<->B, B<->C
#    B<->C, A<->B, B<->C, A<->B


N, M = map(int, input().split())

A = list(map(int, input().split()))# 配列[-1]アクセスしたいので，[0]には0を入れる．
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A[0] = 0
B[0] = 0
C[0] = 0

from collections import deque

q = deque()

q.appendleft((A,B,C,0))

found = -1

while len(q) > 0:
    a,b,c,d = q.popleft()

    print(d, "", a,b,c, len(a), len(b), len(c))

    d += 1

    if d > M+1:
        break
    # A->B
    # B->C
    # C->A
    # B->A
    # C->B
    # A->C

    for fr, to in [("a", "b"), ("b", "a"), ("b", "c"), ("c", "b")]:
        if fr=="a":
            eleFr = a[-1]
        elif fr=="b":
            eleFr = b[-1]
        elif fr=="c":
            eleFr = c[-1]

        if eleFr == 0:
            continue

        if to=="a":
            eleTo = a[-1]
        elif to=="b":
            eleTo = b[-1]
        elif to=="c":
            eleTo = c[-1]

        if eleTo >= eleFr: 
            continue

        copyA = a.copy()
        copyB = b.copy()
        copyC = c.copy()

        if fr=="a":
            copyA.pop(-1)
        elif fr=="b":
            copyB.pop(-1)
        elif fr=="c":
            copyC.pop(-1)

        if to=="a":
            copyA.append(eleFr)
        elif to=="b":
            copyB.append(eleFr)
        elif to=="c":
            copyC.append(eleFr)

        if len(copyA) == N+1 or len(copyC) == N+1:
            break

        q.append((copyA, copyB, copyC, d))

print(found)