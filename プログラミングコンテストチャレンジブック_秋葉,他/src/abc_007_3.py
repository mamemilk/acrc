# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

R,C = map(int, input().split())
sy, sx = map(lambda a: int(a) - 1, input().split())
gy, gx = map(lambda a: int(a) - 1, input().split())
Cyx = []
for i in range(R):
    Cyx.append(input())

q = deque()
checked = [[False for c in range(C)] for r in range(R)]

q.appendleft((sy,sx,0))
checked[sy][sx] = True

while len(q) > 0:
    y,x,d = q.popleft()

    nd = d + 1

    for ny,nx in [(y-1,x),(y,x+1),(y+1,x),(y,x-1)]:
        if not checked[ny][nx] and Cyx[ny][nx]==".":
            q.append((ny,nx,nd))
            checked[ny][nx] = True
        
        if ny==gy and nx==gx:
            print(nd)
            exit(0)