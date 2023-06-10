# https://atcoder.jp/contests/abc104/tasks/abc104_c
# Dが最大値10, Pが最大値100
#
# 解く得点帯を全探索する
# で，結構なやんで，Googleカンニングしました．
# 
# "全部"解く得点帯を全探索する．が簡単そう．

D,G = map(int, input().split())
P = []
C = []
B = []

for d in range(D):
    p,c = map(int, input().split())
    P.append(p)
    C.append(c)
    B.append((d+1)*100+c)

import itertools

Seq = range(D)

res = []

for n in range(0, D+1):
    for comb in itertools.combinations(Seq, n):
        print(comb)
        offset = sum([B[ele] for ele in comb])
        num =  sum([P[ele] for ele in comb])

        if G - offset > 0:
            offset_b = 0
            d = D
            while G - offset_b - offset> 0:
                num_b_exp = (G - offset_b - offset) // (100 * d)
                if num_b_exp > P[d-1]-1:
                    offset_b += (P[d-1]-1) * (100*d)
                    num += (P[d-1]-1)
                    d -= 1
                else:
                    num += num_b_exp
                    offset_b += num_b_exp * (100*d)
                    d -= 1
        
        res.append(num)
    
print(res)