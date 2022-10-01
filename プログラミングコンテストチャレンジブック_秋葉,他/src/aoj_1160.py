# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
# AOJのアカウント作ってないので，サブミットは未．

def run():
    W,H = map(int, input().split())

    if W == 0 and H == 0:
        return exit(0)

    C = []

    for y in range(H):
        row = list(map(int, input().split()))
        C.append(row)

    def find_o(M):
        for h,row in enumerate(M):
            for w, ele in enumerate(row):
                if ele == 1:
                    return (h,w)
        return (None,None)

    def dfs(y,x,M):
        M[y][x] = 0

        for (ny, nx) in [(y-1,x), (y-1,x+1), (y,x+1), (y+1,x+1), (y+1,x), (y+1,x-1), (y,x-1), (y-1,x-1)]:
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            
            if M[ny][nx] == 1:
                dfs(ny,nx,M)

    count = 0
    while True:
        sy,sx = find_o(C)
        if sy != None:
            count += 1
            dfs(sy,sx, C)
        else:
            break

    print(count)

while True:
    run()