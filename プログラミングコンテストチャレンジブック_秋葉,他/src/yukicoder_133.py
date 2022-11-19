# https://yukicoder.me/problems/199

N = int(input())
As = map(int, input().split())
Bs = map(int, input().split())

def judge(A,B):
    awin = 0
    bwin = 0
    for a,b in zip(A,B):
        if a > b:
            awin += 1
        elif b > a:
            bwin += 1
    return awin > bwin

import itertools

PA = itertools.permutations(As)
PB = itertools.permutations(Bs)

num = 0
numa = 0
for pa in PA:
    for pb in PB:
        num += 1

        if judge(pa, pb):
            numa += 1


print(numa/num)