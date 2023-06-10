# https://atcoder.jp/contests/abc054/tasks/abc054_c
# 
# 全探索する．

import itertools

N, M = map(int, input().split())
AB = []
for i in range(M):
    a,b =  map(int, input().split())
    AB.append((a,b))

p = itertools.permutations(range(2, N+1), N-1)

ans = 0
        
# print(AB)

def check():
    ABtemp = AB.copy()
    for i, s in enumerate(seq[:-1]):
        ns = seq[i+1]

        f = list(filter(lambda ab: (ab[0]==s and ab[1]==ns) or (ab[1]==s and ab[0]==ns), ABtemp))

        if len(f) > 0:
            ABtemp.remove(f[0])
        else:
            return False

    return True


for i in p:
    seq = [1] + list(i)
    #print(seq, check(), AB)
    if check():
        ans += 1

print(ans)
