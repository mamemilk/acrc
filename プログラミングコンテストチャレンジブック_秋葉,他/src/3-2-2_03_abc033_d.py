# https://atcoder.jp/contests/abc033/tasks/abc033_d
# 
# 解説読みました．
# 角度の計算は，複素数表現にして求める．

from cmath import phase, pi

N = int(input())
xyi = [complex(*map(int, input().split())) for _ in range(N)]

error = 1e-9

# print(xyi)

donkaku = 0
chokkaku = 0

for b in xyi:
    angles = sorted([phase(a - b) for a in xyi if a != b])
    # 2周分持つ
    angles += [angle + 2*pi for angle in angles]

    l = 0 
    r = 0
    for s in range(N-1):
        while angles[l] - angles[s] < pi / 2 - error: # sに対して，90度以下になるやつ
            l += 1
        while angles[r] - angles[s] < pi + error: # sに対して，180度以下になるやつ
            r += 1

        if abs(angles[l] - angles[s] - pi/2) < error:
            chokkaku += 1
            l += 1 

        donkaku += r - l


print(N * (N-1) * (N-2) // 6 - chokkaku - donkaku, chokkaku, donkaku)