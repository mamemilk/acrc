# https://atcoder.jp/contests/arc041/tasks/arc041_d
#
# 解説を読む．
# 
# • 始点とはじめの色を全探索する。
# • 深さ優先探索や幅優先探索で貪欲に辺を塗っていく。
# • すべての辺を塗れたら、すぐ “Yes” と判定する。
# • 奇数長の閉路が完成したら、すぐ “Yes” と判定する。
# • そうでなければ “No” と判定する

from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    apre, bpre, c = input().split()
    a = int(apre) - 1
    b = int(bpre) - 1
    G[a].append((b, c))
    G[b].append((a, c))


def bfs(a, c):
    q = deque()
    q.append((a, -1, c)) # 始点，前の点，aからいずれかのbにいくときに塗る色
    ans = 0
    color = [-1 for _ in range(N)]
    while q:
        qa, qprev, qc = q.popleft()
        if color[qa] == -1:
            color[qa] = qc
        else:
            if color[qa] != qc:
                return True
            else:
                continue
 
        for b, bc in G[qa]:
            if b != qprev and bc == qc:
                q.append((b, qa, 'r' if qc == 'b' else 'b')) 
                ans += 1

    return ans == M
 
 
for a in range(M):
    for c in ['r', 'b']:
        if bfs(a, c):
            exit(print("Yes"))
print("No")