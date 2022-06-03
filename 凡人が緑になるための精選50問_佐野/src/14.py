# https://atcoder.jp/contests/abc181/tasks/abc181_c

"""
八木さんの回答は，
傾きが同じかを判別する案．こっちの方が確かに効率的．
"""

import itertools

N = int(input())
XY = []
for n in range(N):
    x,y = map(int, input().split())
    XY.append((x,y))

# sqrtすると，フロートになってしまうため，距離2乗で距離を比較
# A,Bは相対ベクトル
def is_online(A,B):
    # 距離 ^ 2
    na2 = A[0] ** 2 + A[1] ** 2
    nb2 = B[0] ** 2 + B[1] ** 2

    dp = A[0] * B[0] + A[1] * B[1]
    dp2 = dp ** 2 
    if dp2 == na2 * nb2:
        return True
    else:
        return False

is_yes = False
for a,b,c in itertools.combinations(XY, 3):
    A = (a[0] - b[0], a[1] - b[1])
    B = (c[0] - b[0], c[1] - b[1])

    if is_online(A,B):
        print('Yes')
        is_yes = True
        break

if is_yes:
    pass
else:
    print('No')

