# https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_e


# 交点の数の求め方
#    直線がN本ある
#    交点の数は、
#      
#    https://ferin-tech.hatenablog.com/entry/2017/10/01/145114
#      Xs     Xe      
#      1      2   転倒数 0 
#      2      4   転倒数 2 
#      3      3   転倒数 2 
#      4      1   転倒数 3 
#      
#    Xsをここで十分左とすると(-∞)、1,2,3,4の順番は傾きの大きさによって求まる。
# 
# とりうみさんの回答を参考にさせていただいた。
# 
# 傾きの昇順でならべると、x=-infでのy座標降順でならぶが、
# x=mにおけるy座標を並べる際にy座標を降順でならべるためにreverse=Trueとした。
#      x=-inf でのy座標降順 & x=mでのy座標降順    転倒数 = 交差数   ここは上のメモ書き通り
#      x=-inf でのy座標降順 & x=mでのy座標昇順    転倒数 = (物理的に何を意味するか分からないが交差数の対偶的なもの？)
# で、後者でも、二分探索のl,rの更新を変えれば計算可能っぽいんだが、後者の意味がいまいち分からん。
#    
# koutenga kisu, guusu de care ga hituyou 
#    交点の数が偶数か奇数かでケアが必要
#    交点の数が偶数の場合は、交点の数がN*(N-1)/4より大きいかどうかを判定する
#    交点の数が奇数の場合は、交点の数がN*(N-1)/4より大きいかどうかを判定する
#    交点の数がN*(N-1)/4より大きい場合は、交点の数がN*(N-1)/4より大きいかどうかを判定する   

import math

class BinaryIndexedTree:
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.bit[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.bit[index]
            index -= index & -index
        return result

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)


N = int(input())
ABCi = []
for _ in range(N):
    a,b,c = map(int, input().split())
    ABCi.append((a,b,c))

Np = N * (N-1) // 2
target_num = (Np - 1) // 2
# target_num = Np // 2

print(Np, target_num)

# target_num = (N * (N-1) // 2 - 1) // 2

# print("target_num", target_num)

# y = -A/B x + C/B
def binsearch(is_tranp=False):
    # 傾きkの昇順、すなわち、x = - infでのy座標の降順
    if not is_tranp:
        sorted_index = sorted(range(N), key=lambda i: - ABCi[i][0] / ABCi[i][1])
    else:
        sorted_index = sorted(range(N), key=lambda i: - ABCi[i][1] / ABCi[i][0])

    l, r = -2e8, 2e8

    while r - l > 1e-9 and (l == 0 or abs((r - l) / l) > 1e-9):
        m = (l+r)/2
        # y = -A/B x + C/B
        # sorted_indexのindex0がどのindexになるかを求める。
        # ABCi[ sorted_index[i] ]

        # x = mでのy座標の昇順、降順ではなく昇順
        if not is_tranp:
            Ai = sorted(range(N), 
                        key=lambda i: - ABCi[sorted_index[i]][0]/ABCi[sorted_index[i]][1] * m + ABCi[sorted_index[i]][2]/ABCi[sorted_index[i]][1],
                        reverse=True
                        )
        else:
            Ai = sorted(range(N), 
                        key=lambda i: - ABCi[sorted_index[i]][1]/ABCi[sorted_index[i]][0] * m + ABCi[sorted_index[i]][2]/ABCi[sorted_index[i]][0],
                        reverse=True
                        )

        bit = BinaryIndexedTree(N)
        ans = 0 
        for a in map(lambda i:i+1, Ai):
            bit.update(a, 1)
            ans += bit.range_query(a+1, N)

        if ans > target_num:
            r = m
        else: 
            l = m

    return l

print(binsearch(False), binsearch(True))

# find x 