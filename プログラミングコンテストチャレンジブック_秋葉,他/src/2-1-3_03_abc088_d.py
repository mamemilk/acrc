# https://atcoder.jp/contests/abc088/tasks/abc088_d
#
# 経路をきちんと求めてそれ以外を塗る，ということをしそうになったが，
# 距離+1以外マスはぬれるので，H*W - (距離+1) - #の数の数をすればOK．


from collections import deque

R,C = map(int, input().split())
Cyx = []
for i in range(R):
    Cyx.append(input())
    
num_b = 0
for row in Cyx:
    num_b += row.count("#")

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
            if ny >= 0 and ny < R and nx >= 0 and nx < C and not checked[ny][nx] and Cyx[ny][nx]!="#":
                # print(ny,nx,nd)
                q.append((ny,nx,nd))
                checked[ny][nx] = True
            
            if ny==gy and nx==gx:
                return nd

    return -1 


d = a_to_b((0,0), (R-1,C-1))

if d < 0:
    ans = -1
else:
    ans = R*C - num_b - (d+1)

print(ans)

