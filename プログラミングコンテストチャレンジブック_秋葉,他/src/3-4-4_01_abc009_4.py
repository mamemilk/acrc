# https://atcoder.jp/contests/abc009/tasks/abc009_4
# 一応自力
# 単位行列が、1ではなく、fullbit立ってるやつなのが注意。

K, M = map(int, input().split())
Ai = list(map(int, input().split()))
Ci = list(map(int, input().split()))

import numpy as np
mat = np.zeros((K, K), dtype=np.uint32)
mat[0] = Ci
for i in range(1, K):
    # 単位行列が1ではなく、fullbit立ってるやつ
    mat[i][i-1] = (1<<32)-1

def logic_matmul(A, B):
    ans = np.zeros((K, K), dtype=np.uint32)
    for m in range(K):
        for n in range(K):
            tmp = 0
            for k in range(K):
                tmp ^= A[m][k] & B[k][n]
            # print("?", A[m], B[:,n], tmp)
            ans[m][n] = tmp
    return ans

max_p = int(np.log2(M - K))
mat_powers = [mat]
for i in range(1, max_p+1):
    mat_powers.append(logic_matmul(mat_powers[-1], mat_powers[-1]))

tmp = mat
res = M - K - 1

while res > 0:
    l = int(np.log2(res))
    tmp = logic_matmul(tmp, mat_powers[l])
    # print(res, l, 2**l, '\n', tmp)

    if l == 0:
        break
    res -= 2**l

ans = 0 
for k in range(K):
    ans ^= tmp[0][k] & Ai[::-1][k]
print(ans)

