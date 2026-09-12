# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_f
# 
# 

N, X, Y, Z = map(int, input().split())
MOD = 10 ** 9 + 7

if N > X + Y + Z: # 全員は就職できない。
    print(0)
    exit()

# 0! 〜 N! と逆数を前計算
fact = [1] * (N + 1)
for i in range(2, N + 1):
    fact[i] = i * fact[i-1] % MOD
fact_inv = [1] * N + [pow(fact[N], -1, MOD)]
for i in range(N, 2, -1):
    fact_inv[i-1] = i * fact_inv[i] % MOD

# (c1, c2, c3) の組における 1 / (yz!zx!xyz!) の和を前計算
C1 = min(Y + Z, N)
C2 = min(Z + X, N)
A = [[[0] * (N + 1) for _ in range(C2 + 1)] for _ in range(C1 + 1)]
for yz in range(C1 + 1):
    for zx in range(C2 + 1):
        v = fact_inv[yz] * fact_inv[zx] % MOD
        for c3 in range(N + 1):
            xyz = c3 - yz - zx
            if xyz >= 0:  A[yz][zx][c3] += v * fact_inv[xyz] % MOD
            if yz:        A[yz][zx][c3] += A[yz-1][zx][c3]
            if zx:        A[yz][zx][c3] += A[yz][zx-1][c3]
            if yz and zx: A[yz][zx][c3] -= A[yz-1][zx-1][c3]
            A[yz][zx][c3] %= MOD

# 条件を満たす全ての（x, y, z, xy, yz, zx, xyz) の組における
# N! / (x!y!z!xy!yz!zx!xyz!) の和を求める
ans = 0
for x in range(min(X, N) + 1):
    v1 = fact[N] * fact_inv[x] % MOD
    for y in range(min(Y, N - x) + 1):
        v2 = v1 * fact_inv[y] % MOD
        for z in range(min(Z, N - x - y) + 1):
            v3 = v2 * fact_inv[z] % MOD
            for xy in range(min(X + Y, N - z) - x - y + 1):
                v4 = v3 * fact_inv[xy] % MOD
                c3 = N - x - y - z - xy
                c1 = min(Y + Z - y - z, c3)
                c2 = min(Z + X - z - x, c3)
                ans += v4 * A[c1][c2][c3] % MOD
                ans %= MOD
print(ans)