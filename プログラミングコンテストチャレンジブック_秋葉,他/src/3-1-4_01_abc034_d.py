# https://atcoder.jp/contests/abc034/tasks/abc034_d

N, K = map(int, input().split())
wpgi = []
for _ in range(N):
    w,p = map(int, input().split())
    wpgi.append((w,p))

ok = 0
ng = 100

for _ in range(100):
    mid=(ok+ng)/2
    a = []
    for w,p in wpgi:
        a.append((p-mid)*w)
    a.sort(reverse=True)
    # print(a)
    
    if sum(a[:K])>=0:
        ok=mid
    else:
        ng=mid

print(ok)