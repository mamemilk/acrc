# https://atcoder.jp/contests/atc001/tasks/dfs_a

H,W = map(int, input().split())
M = []
for h in range(H):
    yoko = list(input())
    if 'g' in yoko:
        G = (h, yoko.index('g'))
    if 's' in yoko:
        S = (h, yoko.index('s'))
    M.append(yoko)

is_found = False

nexts = set([G])

while len(nexts) > 0 : 
    next_nexts = set()

    for (y,x) in nexts:
        M[y][x] = 'g'

    for (y,x) in nexts:
        for (ny, nx) in [(y-1,x), (y,x+1), (y+1,x), (y,x-1)]:
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
        
            if M[ny][nx] == '.':
                next_nexts.add((ny,nx))
            if M[ny][nx] == 's':
                is_found = True
                break
        nexts = next_nexts

print("Yes" if is_found else "No")