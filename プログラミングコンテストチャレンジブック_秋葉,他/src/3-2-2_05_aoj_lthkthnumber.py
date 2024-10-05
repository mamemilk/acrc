# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0646
# 
# 解説読んだ上に，人の回答を見ました．
# https://www2.ioi-jp.org/joi/2017/2018-yo/2018-yo-t6-review.html
# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4221870#1
# 
# 
'''
それでは，xが与えられたとき書きだされた数の中でx以下の数がいくつあるかを求めてみよう．
33点の解法で述べたとおり，左端lから右端rの中でのK番目の数がx以下のとき，右端を伸ばしてもK番目の数はx以下のままである．
すなわち，ある左端lについてK番目の数がx以下になる最小のrを求めることで，ある左端lについてはx以下が(N+1-r)回書かれることが分かる．
'''


N, K, L = map(int, input().split())
ai = [*map(int, input().split())]


def solve(x):
    arr = []
    res= 0
    for t, _ in enumerate(ai):
        if ai[t] <= x:
            arr.append(t)
        if len(arr) >= K:
            res += arr[-K] + 1
    return res >= L

l = 0
r = N
while l + 1 < r:
    mid = (l+r) // 2
    if solve(mid):
        r = mid
    else:
        l = mid
print(r)
