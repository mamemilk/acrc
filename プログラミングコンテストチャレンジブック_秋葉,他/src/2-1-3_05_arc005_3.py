# https://atcoder.jp/contests/arc005/tasks/arc005_3
# 
# このリンクを読む．
# 壁がない場合は移動距離0，壁のマスを通る場合は移動距離1で，最短距離が2なら通れる．
# https://betrue12.hateblo.jp/entry/2018/12/08/000020


from collections import deque

R,C = map(int, input().split())
Cyx = []
for i in range(R):
    Cyx.append(input())
    
q = deque()
checked = [[False for c in range(C)] for r in range(R)]



def findS(s):
    for r, row in enumerate(Cyx):
        if s in row:
            sy,sx = r,row.index(s)
            return sy,sx

def bfs01(a, b):

    sy,sx = a
    gy,gx = b

    q = deque()
    checked = [[False for c in range(C)] for r in range(R)]

    q.appendleft((sy,sx,0))
    checked[sy][sx] = True

    while len(q) > 0:
        y,x,d = q.popleft()

        for ny,nx in [(y-1,x),(y,x+1),(y+1,x),(y,x-1)]:
            if ny >= 0 and ny < R and nx >= 0 and nx < C and not checked[ny][nx]:
                if Cyx[ny][nx] =="#":
                    q.append((ny,nx,d + 1))
                    checked[ny][nx] = True
                else:
                    q.appendleft((ny,nx,d))
                    checked[ny][nx] = True
            
            if ny==gy and nx==gx:
                return d

sy,sx = findS("s")
gy,gx = findS("g")

res = bfs01((sy,sx), (gy,gx))

if res <= 2:
    print("YES")
else:
    print("NO")