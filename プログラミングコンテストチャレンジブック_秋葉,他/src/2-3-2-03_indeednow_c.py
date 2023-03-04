# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_c

N, M = map(int, input().split())

# 0~100=>101. + 1 de 102
DP = [[[0] * 102 for i in range(102)] for j in range(102)]

for _ in range(N):
    a,b,c,w = map(int, input().split())
    DP[a][b][c] = max(DP[a][b][c], w) # choufuku check 

for i in range(101):
    for j in range(101):
        for k in range(101):
            DP[i+1][j][k] = max(DP[i+1][j][k], DP[i][j][k])
            DP[i][j+1][k] = max(DP[i][j+1][k], DP[i][j][k])
            DP[i][j][k+1] = max(DP[i][j][k+1], DP[i][j][k])

XYZ = []
for _ in range(M):
    x,y,z = map(int, input().split())
    XYZ.append((x,y,z))

for x,y,z in XYZ:
    print(DP[x][y][z])