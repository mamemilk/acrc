# https://atcoder.jp/contests/tenka1-2015-quala/tasks/tenka1_2015_qualA_c
# 
# A, Bのモザイクアートがあったときに，
#   - 白，黒の反転
#   - 4近傍の交換   : 2個をコスト1で変更できる
# がそれぞれコスト1で，A，Bを一致させるコストを求める
# 
# 最小コスト = 不一致マス数 − 最大マッチング数

import sys

sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
B = [list(map(int, input().split())) for _ in range(M)]

# 不一致を2種類に分ける
# 左側：A=0, B=1
# 右側：A=1, B=0

left_id = [[-1] * N for _ in range(M)]
right_id = [[-1] * N for _ in range(M)]

left_count = 0
right_count = 0
mismatch_count = 0

for i in range(M):
    for j in range(N):
        if A[i][j] == B[i][j]:
            continue

        mismatch_count += 1

        if A[i][j] == 0 and B[i][j] == 1:
            left_id[i][j] = left_count
            left_count += 1
        else:
            right_id[i][j] = right_count
            right_count += 1


# 二部グラフを構築する
# 左側の不一致と右側の不一致が上下左右に隣接していたら、
# 交換1回で両方を直せるので辺を張る
graph = [[] for _ in range(left_count)]

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

for i in range(M):
    for j in range(N):
        left = left_id[i][j]

        if left == -1:
            continue

        for di, dj in directions:
            ni = i + di
            nj = j + dj

            if not (0 <= ni < M and 0 <= nj < N):
                continue

            right = right_id[ni][nj]

            if right != -1:
                graph[left].append(right)


# match[v] 右側の頂点 v とマッチしている左側の頂点
# マッチしていなければ -1
match_right = [-1] * right_count
visited = [0] * right_count

def dfs(left, visit_number):
    for right in graph[left]:
        if visited[right] == visit_number:
            continue

        visited[right] = visit_number

        # 右側頂点が未使用なら、そのままマッチングする
        if match_right[right] == -1:
            match_right[right] = left
            return True

        # 現在の相手を別の右側頂点へ移動できるか試す
        previous_left = match_right[right]

        if dfs(previous_left, visit_number):
            match_right[right] = left
            return True

    return False


# 最大二部マッチング
matching_count = 0

for left in range(left_count):
    visit_number = left + 1

    if dfs(left, visit_number):
        matching_count += 1

# 最初はすべての不一致を個別に色変更すると考える
# 交換ペアを1組作るごとに、コストを1節約できる
answer = mismatch_count - matching_count

print(answer)