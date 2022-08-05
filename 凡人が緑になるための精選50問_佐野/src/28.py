# https://atcoder.jp/contests/abc173/tasks/abc173_c
# #がK個残る選び方．
# 削除する行，列が複数行になるが難しい． 
# 全探索するとしたら，
#   (6C1 + 6C2 + 6C3 + 6C4 + 6C5)^2
# 全探索することにする．

import itertools

H,W,K = map(int, input().split())
C = []
for i in range(H):
    C.append(input().strip())

black_num = sum([line.count('#') for line in C])
#print(black_num)

ans = 0

yiter = []
for i in range(H):
    yiter.append(itertools.combinations(range(H), i))
yiter = itertools.chain(*yiter)

xiter = []
for i in range(W):
    xiter.append(itertools.combinations(range(W), i))
xiter = itertools.chain(*xiter)

for Y,X in itertools.product(yiter, xiter):
    
    bnum_row = 0
    for y in Y:
        bnum_row += C[y].count('#')
    bnum_column =0
    for x in X:
        bnum_column += [C[_y][x] for _y in range(H)].count('#')
    
    double_counted = 0
    for y,x in itertools.product(Y,X):
        if C[y][x] == '#':
            double_counted +=1 

    if black_num - (bnum_row + bnum_column - double_counted) == K:
        ans += 1

print(ans)
