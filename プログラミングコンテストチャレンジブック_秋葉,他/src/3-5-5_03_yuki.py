# https://yukicoder.me/problems/no/421

import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
S = [input() for _ in range(N)]

white_id = [[-1] * M for _ in range(N)]
black_id = [[-1] * M for _ in range(N)]

white_count = 0
black_count = 0

# 白・黒それぞれに一次元IDを割り当てる
for i in range(N):
    for j in range(M):
        if S[i][j] == "w":
            white_id[i][j] = white_count
            white_count += 1

        elif S[i][j] == "b":
            black_id[i][j] = black_count
            black_count += 1


# graph[white]：
# 白頂点whiteと隣接している黒頂点の一覧
graph = [[] for _ in range(white_count)]

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

for i in range(N):
    for j in range(M):
        white = white_id[i][j]

        if white == -1:
            continue

        for di, dj in directions:
            ni = i + di
            nj = j + dj

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            black = black_id[ni][nj]

            if black != -1:
                graph[white].append(black)


# match_black[black]：
# 黒頂点blackとペアになっている白頂点
match_black = [-1] * black_count

visited = [0] * black_count

def dfs(white, visit_number):
    for black in graph[white]:
        if visited[black] == visit_number:
            continue

        visited[black] = visit_number

        if match_black[black] == -1:
            match_black[black] = white
            return True

        previous_white = match_black[black]

        if dfs(previous_white, visit_number):
            match_black[black] = white
            return True

    return False

# 最大マッチング
matching_count = 0

for white in range(white_count):
    if dfs(white, white + 1):
        matching_count += 1

# 方法3
answer = 100 * matching_count

remaining_white = white_count - matching_count
remaining_black = black_count - matching_count

# 方法2
normal_pairs = min(remaining_white, remaining_black)
answer += 10 * normal_pairs

remaining_white -= normal_pairs
remaining_black -= normal_pairs

# 方法1
answer += remaining_white + remaining_black

print(answer)