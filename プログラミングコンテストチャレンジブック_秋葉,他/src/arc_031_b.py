# https://atcoder.jp/contests/arc031/tasks/arc031_2
# 埋めるマスは結局全探索になってしまった．
#   - DFSなので，マスによってはすぐ終わる．特に埋め立て地からスタートするのでDFS関数はすぐに抜ける．
#   - 10x10マスで小さい
# ということで，全探索でもなんとかなった．


A = []

W = 10
H = 10

for h in range(H):
    yoko = list(input())
    A.append(yoko)

def dfs(y,x,M):
    M[y][x] = '.'

    for (ny, nx) in [(y-1,x), (y,x+1), (y+1,x), (y,x-1)]:
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        
        if M[ny][nx] == 'o':
            dfs(ny,nx,M)

def find_o(M):
    for h,row in enumerate(M):
        for w, ele in enumerate(row):
            if ele == 'o':
                return (h,w)
    return (None,None)

for y in range(H):
    for x in range(W):
        M = [[ele for ele in row] for row in A]
        
        if M[y][x] == 'x':
            M[y][x] = 'o'
            sy,sx = find_o(M)

            if sy != None:
                dfs(sy,sx,M)

                nsy, nsx = find_o(M)

                if nsy == None:
                    print("YES")
                    exit(0)

print("NO")