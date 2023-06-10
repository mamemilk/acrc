# https://atcoder.jp/contests/abc038/tasks/abc038_d
# 
# 
# wで昇順で並べる．並び替えた列の，hのLONGEST INCREASING SEQUENCEを求める．
# - wが等しい2要素を除去できず
# - LISを求める方法
# で詰まって，以下のページをカンニングしてしまう．
# https://soohprogramming.wordpress.com/2020/11/13/abc038-d-%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E3%83%88/
# 
# 前者は，wの後にhを降順に並べると，同一のwから選択される要素は一つにできる．
# 後者は，蟻本のP.64を見ました．蟻本一版のdp[j] は，dp[j+1]の誤植?

N = int(input())
WH = []
for _ in range(N):
    w,h = map(int, input().split())
    WH.append((w,h))

WH.sort(key=lambda ele: (ele[0], -ele[1]))

Hs = [ele[1] for ele in WH]

# print(WHs)

def LIS(arr):
    dp = [0] * (len(arr)+1)
    for index,a  in enumerate(arr):
        dp[index+1] = 1
        # print("index, a", index, a, dp)
        for j in range(index):
            # print(index, j, dp, arr[j], a)
            if arr[j] < a:
                dp[index+1] = max(dp[index+1], dp[j+1]+1)
    return dp

print(LIS(Hs)[-1])