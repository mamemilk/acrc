# https://atcoder.jp/contests/abc193/tasks/abc193_c

"""
全探索の計算量は，O(N^2)なので，全探索とする．
ただ，a,bの値域を絞らないと遅くて，通らなかったので，値域を絞る．

以下は，1の桁の判別で何かしら早くできないかと思ったが，全探索で通ったので備忘録としてのみ残す．
       a
b = 1  0 1 2 3 4 5 6 7 8 9 
b = 2  0 1 4 9 6 5 6 9 4 1
b = 3  0 1 6 1 6 5 6 1 6 1
b = 4  0 1 6 1 6 5 6 1 6 1

       0 1 2 3 4 5 6 7 8 9 
b = 2  O O - - O O O - - O
b = 3~ O O - - - O O - - -  
"""

import math

N = int(input())

set_n = set()

sqrt_n_int = int(math.sqrt(N))

for a in range(2,sqrt_n_int+1,1):
    for b in range(2,33+1,1):
        tmp = a**b
        if tmp > N:
            break        
        set_n.add(tmp)

print(N - len(set_n))
