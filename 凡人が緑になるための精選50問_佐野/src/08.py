#https://atcoder.jp/contests/abc192/tasks/abc192_c

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))
    
def g2(x):
    return int(''.join(sorted(str(x), reverse=False)))

def f(x):
    return g1(x) - g2(x)

N, K = map(int, input().split())

a = N
for n in range(K):
    a = f(a)

print(a)