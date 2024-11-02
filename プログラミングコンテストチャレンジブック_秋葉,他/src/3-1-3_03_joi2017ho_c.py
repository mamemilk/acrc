# https://atcoder.jp/contests/joi2017ho/tasks/joi2017ho_c

# 
# 鳥海さんの回答をカンニング．
H, V = map(int, input().split())
M = []
for _ in range(V):
    M.append([*map(int, input().split())])



def is_possible(A, upper, lower):
    for a in A:
        h = len(a)
        w = len(a[0])
        prev_b = w
        for i in range(h):
            b = 0
            for j in range(prev_b):
                if a[i][j] > upper:
                    break
                b += 1
            if i == 0 and b == 0:
                break
            for j in range(b, w):
                if a[i][j] < lower:
                    break
            else:
                prev_b = b
                continue
            break
        else:
            return True
    return False
                
H, W = map(int, input().split())
A = [[] for _ in range(4)]
low = 10**9
high = 1
for _ in range(H):
    row = list(map(int, input().split()))
    low = min(low, min(row)) 
    high = max(high, max(row))
    A[0].append(row)

A[1] = [[row[i] for row in A[0][::-1]] for i in range(W)]
A[2] = [row[::-1] for row in A[0][::-1]]
A[3] = [row[::-1] for row in A[1][::-1]]

l = 0
r = high - low - 1
while l <= r:
    d = (l + r) // 2
    if is_possible(A, low + d, high - d):
        r = d - 1
    else:
        l = d + 1
print(l)
