# https://atcoder.jp/contests/abc002/tasks/abc002_4
# 議員数が，N<=12と少ない
# 
# 知り合い候補を作って，それが成立するを全探索する．のが愚直だが実装できそう．
# 他にスマートな方法思いつかず．


import itertools

N, M = map(int, input().split())
C = []
for _ in range(M):
    x,y = map(int, input().split())
    C.append((x,y))

# print(C)
Seq = list(range(1,N+1))

for n in range(N, 1, -1):
    # print(n)
    for comb in itertools.combinations(Seq, n):
        hoge = list(itertools.combinations(comb, 2))

        for c in C:
            if c in hoge:
                hoge.remove(c)

        if len(hoge) == 0:
            print(n)
            exit(0)
    
print(1)