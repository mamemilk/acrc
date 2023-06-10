# https://www.ioi-jp.org/joi/2009/2010-ho-prob_and_sol/2010-ho.pdf#page=11

N, H = map(int, input().split())
DH = []
for _ in range(N-1):
    d, h = map(int, input().split())
    DH.append((d,h))

maxH = H
ans = 0
# greedy に最小限healする
for (index, (d,h)) in enumerate(DH):
    preH = H
    if H > d:
        pass # no heal
    else:
        tmp = (d - H + 1 + h - 1) // h
        ans += tmp
        H += h * tmp
        H = min(H, maxH)
    H -= d
    print(index, d, h, preH, '->', H, ans)

print(H, ans)
