# https://codeforces.com/contest/462/problem/C
# TLEが解消せず．時間切れ．

_ = input()
Ni = list(map(int, input().split()))
Ni.sort(reverse=True)

ans = 0
while len(Ni) > 0:
    ans += sum(Ni)
    m = Ni.pop() # min(Ni)
    # Ni.remove(m)
    if len(Ni) != 0:
        ans += m
print(ans)