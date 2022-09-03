'''
https://atcoder.jp/contests/abc197/tasks/abc197_c

2分割だけでなく，n分割される．
PyPyで，TLEを回避した．

本当はメモ化と再帰でかきたかったが，ここは諦めた．

'''

from functools import reduce

N = int(input())
Seq = list(map(int, input().split()))

candid = []

def spl(seq):
    n = len(seq) - 1
    a = []
    for i in range(2 ** n):
        b = []
        tmp = []
        for j in range(n):
            tmp.append(seq[j])
            if (i >> j) & 1:
                b.append(tmp)
                tmp = []
                k = j
        tmp.append(seq[-1])
        b.append(tmp)
        yield b
        #a.append(b)
    #return a

candid = []
for i in spl(Seq):
    # if len(i) == 1:
    #     continue

    tmp_xor = 0
    for j in i: # i = [[1], [5, 7]] etc
        tmp_or = reduce(lambda a,b: a | b, j)
        tmp_xor = tmp_xor ^ tmp_or
    candid.append(tmp_xor)

print(min(candid))

# for i in range(1,N):
#     a = Seq[:i]
#     b = Seq[i:]
#     or_a = reduce(lambda a,b: a | b, a)
#     or_b = reduce(lambda a,b: a | b, b)
#     candid.append((or_a ^ or_b, i, ))

# hoge = min(candid, key=lambda ele:ele[0])
# print(hoge[0])
    