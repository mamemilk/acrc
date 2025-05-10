# https://atcoder.jp/contests/arc076/tasks/arc076_d
# 
# Segment Treeで解けず、他の方法で解けるかカンニング。
# Greedyで解けるっぽいが、実装内容をまだ理解できておらず。


from heapq import heappush, heappop

# N : number of Takahashi-kuns
# M : number of seats
N, M = map(int, input().split())

LRs = [list(map(int, input().split())) for _ in range(N)]
LRs.sort(key=lambda LR: LR[1])

ans_left = 0
index = 1
for L, R in LRs:
    if R==M+1 or index==M+1:
        break
    ans_left += 1
    index = max(index+1, R+1)

index_LR = 0
q = []
for i in range(M+1-ans_left, M+1):
    while index_LR<N and LRs[index_LR][1]<=i:
        l, L = LRs[index_LR]
        heappush(q, l)
        index_LR += 1
    heappop(q)
while index_LR<N:
    l, L = LRs[index_LR]
    q.append(l)
    index_LR += 1

q.sort(reverse=True)
ans_right = 0
index = M
for l in q:
    if l==0 or index==0 or ans_right+ans_left==M:
        break
    ans_right += 1
    index = min(l-1, index-1)
ans = N - ans_left - ans_right
print(ans)