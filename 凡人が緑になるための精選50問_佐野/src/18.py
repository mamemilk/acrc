# https://atcoder.jp/contests/abc177/tasks/abc177_c

"""
ai*ajのかけ算でやると，時間が足りない．多分，そこが意図．
ai * sum(aj)的な感じでやる．

とか言って，提出したら，実行時間変わらず．
なので，メモ化をする．
"""

import itertools

N = int(input())
A = list(map(int, input().split()))

res = 0
sum_j = 0

for i in range(N-2,-1,-1):
    sum_j += A[i+1]
    res  += sum_j * A[i]

res = res %  (10**9 + 7)    

print(res)