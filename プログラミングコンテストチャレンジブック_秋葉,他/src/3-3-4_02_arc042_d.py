# https://atcoder.jp/contests/arc042/tasks/arc042_d
#
# 解説みても，baby step, giant stepの説明見ても，よくわからなかったが，
# 以下動画が理解に役に立った．
# https://www.youtube.com/watch?v=007MVsELvQw
# 
# a^x ≡ b (mod N) で，xを求めたいとき，
# 
# a^k ≡ b(3)^l となるk, lのペアを求めれば，
# a^(k+l) ≡ bとなるので，k+lが答えになる．
#  
#
# TLE 6, WA 2が残っている．

import math

# X^K ≡ Y (mod M) となるような K を求める
def baby_step_giant_step(X, Y, M):
    # Baby step
    m = math.ceil(math.sqrt(M-1))

    table = {1:0} # keyがmod, valueがK, X^0 = 1
    z = 1
    for i in range(1, m):
        z = (z * X) % M
        table[z] = i

    # print(table)

    if Y in table:
        return table[Y]

    c = pow(X, m * (M-2), M)
    for j in range(m):
        y = (Y * pow(c, j, M)) % M
        if y in table:
            return j * m + table[y]

    return None

# assert baby_step_giant_step(3, 19, 59) == 17
# assert baby_step_giant_step(3, pow(3, 12, 17), 17) == 12
# assert baby_step_giant_step(12, pow(12, 17, 101), 101) == 17

# X^i (A<= i <=B)で，mod Pでのあまりが最小になるiを求める．
# X^i = N (mod P)
X, P, A, B = map(int, input().split())

def solve(X, P, A, B):
    # B - Aが小さい場合 => range(A, B+1)を試す．

    # B - Aが大きい場合 => y を1から試していく．
    #   

    if B - A < 2**24:
        n = pow(X, A-1, P)
        n_min = n
        for i in range(A, B+1):
            n = (n * X) % P
            n_min = min(n_min, n)
        return n_min
    else:
        y = 1
        while True:
            i = baby_step_giant_step(X, y, P)
            if (A <= i and i <=B) or (A <= i + P and i + P <= B): 
                return y 

print(solve(X, P, A, B))