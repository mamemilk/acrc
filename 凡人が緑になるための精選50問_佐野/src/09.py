#https://atcoder.jp/contests/abc186/tasks/abc186_c

N = int(input())

res = 0
for n in range(1, N+1):
    if '7' in str(n) or '7' in oct(n):
        pass
    else:
        res += 1

print(res)