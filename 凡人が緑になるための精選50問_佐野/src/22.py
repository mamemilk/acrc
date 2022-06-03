# https://atcoder.jp/contests/abc154/tasks/abc154_d
# 期待値は，(pi + 1) / 2
# この配列から，合計が最大となる隣接するK個を選択する．
# 高速化のために，左端を引いてから右端を足す工夫をしてみる．
# -> index iまでの総和をもっておいて，i+7の総和 - iの総和で求める方がスマートかもしれない．

# N = 7
# index of Pn       = 0 1 2 3 4 5 6 
# K = 3
# index of filt     = 0 1 2 3 4
#                             N-K

N, K = map(int, input().split())
P_post = list(map(lambda p : (int(p) + 1)/2 , input().split()))

filt = []
k_sum = sum(P_post[0:K])
filt.append(k_sum)

for i in range(1,N-K+1):
    k_sum -= P_post[i-1]
    k_sum += P_post[i+(K-1)]
    filt.append(k_sum)

res = max(filt)
print(res)
