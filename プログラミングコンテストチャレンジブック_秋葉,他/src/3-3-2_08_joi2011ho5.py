# https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho5
# 解説読み、さらにカンニングする。
#  aK+1​ から aN​ まで X−1 個選んで総和を bK​×X−aK​ 以下にできるか
# 最小値を求めるのにBITがつかえそうだが、前の二問でBITでの最小値をもとめるのがうまくいっておらず、みんなに習ってヒープを使う。
# 

import heapq

N = int(input())
q = []
heapq.heapify(q)

# ascending order by a
AB = sorted([tuple(map(int, input().split())) for _ in range(N)])

ans = 0
s = 0 
for a,b in AB:
    heapq.heappush(q, (b, a))
    s += a
    # q[0][0] ヒープの中の最小のb
    while q and s > q[0][0]*len(q): # death条件から抜け出すまでPOP, 弱い微生物からPop
        b0, a0 = heapq.heappop(q)
        s -= a0 
    ans = max(ans, len(q))
print(ans)