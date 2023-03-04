# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
# 私の最初のコードでは，マージソート部分がバグってた．鳥海さんご指摘の通り直してAC.
# popするタイミングと，lenの評価タイミングが違うのがそもそものバグの温床っぽかった．

N = int(input())
Pi = list(map(int, input().split()))
Pi.sort()

DP = [[] for _ in range(N)]
DP[0] = [0, Pi[0]]
for n in range(1, N):
    num = Pi[n]

    a = [ele       for ele in DP[n-1]]
    b = [ele + num for ele in DP[n-1]]

    # 重複チェック付きのmerge sortをしている。
    tmp = []
    front_a = a.pop(0)
    front_b = b.pop(0)
    while front_a != None:
        if front_a == front_b:
            tmp.append(front_a)
            front_a = None
            front_b = None
        elif front_a < front_b:
            tmp.append(front_a)
            front_a = None
        else:
            tmp.append(front_b)
            front_b = None

        if front_a == None and len(a) > 0: front_a = a.pop(0)
        if front_b == None and len(b) > 0: front_b = b.pop(0)
    if front_b != None: tmp.append(front_b)
    tmp += b
    
    DP[n] = tmp


print(len(DP[-1]))


# この例だと，len(a) == 0でも，front_aがNone以外が残っている可能性あり．
# a =[1,2,3, 5]
# b =[    3,4,5,  7]みたいなときにだめ．
    # a = [ele       for ele in DP[n-1]]
    # b = [ele + num for ele in DP[n-1]]

    # tmp = []
    # front_a = None
    # front_b = None
    # while len(a) > 0 and len(b) > 0:
    #     if front_a == None: front_a = a.pop(0)
    #     if front_b == None: front_b = b.pop(0)

    #     if front_a == front_b:
    #         tmp.append(front_a)
    #         front_a = None
    #         front_b = None
    #     elif front_a < front_b:
    #         tmp.append(front_a)
    #         front_a = None
    #     else:
    #         tmp.append(front_b)
    #         front_b = None
        
    #     if len(a) == 0:
    #         if front_b != None: tmp.append(front_b)
    #         tmp += b
    #         break
    # DP[n] = tmp