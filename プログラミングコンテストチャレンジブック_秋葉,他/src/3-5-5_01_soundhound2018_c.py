# https://atcoder.jp/contests/soundhound2018/tasks/soundhound2018_c
# 
# ケーニグの定理
# 
# 広告数
# = 全頂点数 - 最小頂点被覆数
# = 全頂点数 - 最大マッチング数
# 
# 最大マッチング
# 「重ならない辺を最大何本選べるか」
#                │
#                │ ケーニグの定理
#                ▼
# 最小頂点被覆
# 「全辺を押さえるために外す最小頂点数」
#                │
#                │ 補集合を取る
#                ▼
# 最大独立集合
# 「互いに隣接しない、広告を置ける最大頂点集合」
#
#

import sys
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
grid = [input() for _ in range(r)]

directions = [
    (-1, 0), # 上
    (1, 0),  # 下
    (0, -1), # 左
    (0, 1),  # 右
]

# (i, j)を1次元アドレッシングする．
def cell_id(i, j):
    return i * c + j

# 市松模様を"左"，"右"で2部に分ける．
# match[v] 右側の頂点 v とマッチしている左側の頂点
# マッチしていなければ -1
match = [-1] * (r * c)

# "左"側のマス (i, j) から増加道を探す
def dfs(i, j):
    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if not (0 <= ni < r and 0 <= nj < c):
            continue

        if grid[ni][nj] == "*":
            continue

        right = cell_id(ni, nj)

        if seen[right]:
            continue
        seen[right] = True

        # 未使用の"右"頂点、または現在の相手を別の場所へ移動できる
        if match[right] == -1:
            match[right] = cell_id(i, j)
            return True

        previous = match[right]
        pi, pj = divmod(previous, c)

        if dfs(pi, pj):
            match[right] = cell_id(i, j)
            return True

    return False

dot_count = sum(row.count(".") for row in grid)
matching_size = 0

# 偶数側を"左"側にする
for i in range(r):
    for j in range(c):
        if grid[i][j] == "." and (i + j) % 2 == 0:
            seen = [False] * (r * c)
            if dfs(i, j):
                matching_size += 1

print(dot_count - matching_size)