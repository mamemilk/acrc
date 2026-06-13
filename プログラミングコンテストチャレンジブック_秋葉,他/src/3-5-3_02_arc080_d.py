# https://atcoder.jp/contests/arc080/tasks/arc080_d
# 
# これも自力は無理。。。

def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

n = int(input())
xs = list(map(int, input().split()))

d = {}
for x in xs:
    for k in (x, x + 1):
        d[k] = d.get(k, 0) ^ 1
S = [k for k, v in d.items() if v]

even = [k for k in S if k % 2 == 0]
odd = [k for k in S if k % 2 == 1]
a, b = len(even), len(odd)

adj = [[] for _ in range(a)]
for i, e in enumerate(even):
    for j, o in enumerate(odd):
        if is_prime(abs(e - o)):
            adj[i].append(j)

match_to = [-1] * b

def dfs(v, used):
    for to in adj[v]:
        if not used[to]:
            used[to] = True
            if match_to[to] == -1 or dfs(match_to[to], used):
                match_to[to] = v
                return True
    return False

m = 0
for v in range(a):
    if dfs(v, [False] * b):
        m += 1

ans = a + b - m
if (a - m) % 2 == 1:
    ans += 1
print(ans)