N, M = map(int, input().split())
ABi = []
for _ in range(M):
    a,b = map(int, input().split())
    ABi.append((a,b))

maxOrder = sorted(ABi, key=lambda ele:ele[1])

ans = 1
_, e_prev = maxOrder[0]

for s, e in maxOrder[1:]:
    if s >= e_prev:
        ans += 1
        e_prev = e

print(ans)
