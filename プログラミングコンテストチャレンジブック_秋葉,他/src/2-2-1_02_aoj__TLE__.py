# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp
#
# 以下のように分割すると時間超過．
# 1 :     
# 2 : 
# 3 : 1 + 2, 3
# 4 : 1 + 3, 2 + 2, 4
# 5 : 1 + 4, 2 + 3, 5
# ....
# 
# 
# 二項に分けた時の初項はコインの最大値まででOKとしてもだめ．


val, m = map(int, input().split())
coins = list(map(int, input().split()))

max_coin = max(coins)
candid = [0] * (val + 1)

for n in range(1, val+1):
    if n == 1:
        candid[n] = 1
    else:
        if n in coins:
            candid[n] = 1
            continue

        pre = float('inf')
        # for (l,r) in [(i, n-i) for i in range(1, n//2+1)]:
        
        for (l,r) in [(i, n-i) for i in range(1, min(n//2+1, max_coin+1))]:
            pre = min(candid[l]+candid[r], pre)
        candid[n] = pre

print(candid[val])