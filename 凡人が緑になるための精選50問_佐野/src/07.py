#https://atcoder.jp/contests/abc197/tasks/abc197_b

H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)

yoko = [s for s in S[X-1]]
tate = [S[y][Y-1] for y in range(H)]

res = 0
# left
for i in range(Y-1, 0-1, -1):
    if yoko[i] == '.':
        res += 1
    else:
        break

# right 
for i in range(Y-1, W, 1):
    if yoko[i] == '.':
        res += 1
    else:
        break


# up
for i in range(X-1, 0-1, -1):
    if tate[i] == '.':
        res += 1
    else:
        break

# down
for i in range(X-1, H, 1):
    if tate[i] == '.':
        res += 1
    else:
        break

res -= 3 if yoko[Y-1] == '.' else 0

print(res)