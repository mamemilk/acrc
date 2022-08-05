# https://atcoder.jp/contests/abc178/tasks/abc178_c
# Nが大きい．
# 最初数えてしまい,演算時間間に合わず.
# 
# 0,9がそれぞれ少なくとも一つ入ってるN桁の数.
# 
# 9がない
# 0がない.
# 0,9がない
# 0,9がそれぞれ1つ以上入ってる.

N = int(input())

print((10**N - (9**N + 9**N - 8**N))%(1000000000+7))
exit(0)



# 以下，数えてしまったときの記録
# 
# 総当たりでやると，計算量は，O(N^2)になりそう．
# 何か工夫をする．

# 例えば N = 3の場合
# 0 9 [1-8] = 8^1
# 9 0 [1-8] = 8^1
# 0 [1-8] 9 
# 9 [1-8] 0
# [1-8] 0 9 
# [1-8] 9 0
# 0 0 9
# 0 9 0
# 9 0 0
# 0 9 9
# 9 0 9 
# 9 9 0

from itertools import combinations
import operator as op
from functools import reduce

# nCrはコピペ
# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom 

N = int(input())

res = 0
for num_0 in range(1,N):
    for num_9 in range(1,N-num_0+1):
        num_18 = N - num_0 - num_9

        # a = len(combinations(range(N), num_0 + num_9)) * len(combinations(range(num_0 + num_9), num_0))
        a = ncr(N, num_0 + num_9) * ncr(num_0 + num_9, num_0)

        continue

        if num_18 == 0:
            res += a
        else:
            res += a + (8 ** num_18)
        

print(res)