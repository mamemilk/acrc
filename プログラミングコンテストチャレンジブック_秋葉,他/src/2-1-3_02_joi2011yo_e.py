# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
# 
# 堅さが1,2,3,4,...,Nのチーズを順番に食べていく，
# S=>1, 1=>2，，，の最短距離を足していく



from collections import deque

R,C,N = map(int, input().split())
Cyx = []
for i in range(R):
    Cyx.append(input())


def findS(s):
    for r, row in enumerate(Cyx):
        if s in row:
            sy,sx = r,row.index(s)
            return sy,sx

def a_to_b(a, b):

    sy,sx = a
    gy,gx = b

    q = deque()
    checked = [[False for c in range(C)] for r in range(R)]

    q.appendleft((sy,sx,0))
    checked[sy][sx] = True

    while len(q) > 0:
        y,x,d = q.popleft()

        nd = d + 1

        for ny,nx in [(y-1,x),(y,x+1),(y+1,x),(y,x-1)]:
            if ny >= 0 and ny < R and nx >= 0 and nx < C and not checked[ny][nx] and Cyx[ny][nx]!="X":
                # print(ny,nx,nd)
                q.append((ny,nx,nd))
                checked[ny][nx] = True
            
            if ny==gy and nx==gx:
                return nd

sy,sx = findS("S")

ans = 0
for i in range(1,N+1):
    gy,gx = findS(str(i))
    res = a_to_b((sy,sx), (gy,gx))
    ans += res
    sy,sx = gy,gx
    
print(ans)    
    