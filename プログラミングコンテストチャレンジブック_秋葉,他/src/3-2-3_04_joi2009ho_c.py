# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_c
# 
# 解説読みました．

# n : 縦棒本数
# m : 横棒本数
# h : 縦棒の長さ
# k : j君が何本目まで選ぶか
n, m, h, k = map(int, input().split()) 

scores = [int(input()) for _ in range(n)]

lines = [tuple(map(int,input().split())) for _ in range(m)]
lines = sorted(lines, key=lambda x: x[1])

# 下から順にscoreを入れ替える
# 一番上で得点がわかるようになる．
for line in lines[::-1]:
    y = line[0]-1
    scores[y],scores[y+1] = scores[y+1],scores[y]

# 横棒を取った場合も，scoreが入れ替わる．が，すいません，間に合わず．
