# https://atcoder.jp/contests/agc033/tasks/agc033_a
#
# BFSにおいて，Qが無くなったとき(全部訪問済みの時)の操作回数を求めればよい．
# python3だと，1.1msecでTLE．Pypyを使ってしまった．
# 速くする方法，あるかなー??

from collections import deque

R,C = map(int, input().split())
Cyx = []
for i in range(R):
    Cyx.append(input())
    
q = deque()
checked = [[False for c in range(C)] for r in range(R)]

for r, row in enumerate(Cyx):
    for c, col in enumerate(row):
        if col == "#":
            q.appendleft((r,c,0))
            checked[r][c] = True
#print(q)

while len(q) > 0:
    y,x,d = q.popleft()

    nd = d + 1

    for ny,nx in [(y-1,x),(y,x+1),(y+1,x),(y,x-1)]:
        if ny >= 0 and ny < R and nx >= 0 and nx < C and not checked[ny][nx]: # and Cyx[ny][nx]!="#":
            # print(ny,nx,nd)
            q.append((ny,nx,nd))
            checked[ny][nx] = True
            
print(nd-1)
