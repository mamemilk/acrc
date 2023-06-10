# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp

N, W = map(int, input().split())
VWi = []
for i in range(N):
    v, w = map(int, input().split())
    VWi.append({'index':i, 'val':v, 'wei':w})


# 全探索
def all_search(i, w):
    if i < 0:
        return {'val': 0, 'wei': 0}

    if w <= 0: 
        return {'val': 0, 'wei': 0}

    # case a: iをつかうときー
    res_a = all_search(i-1, w-VWi[i]['wei'])
    val_a = res_a['val'] + VWi[i]['val']
    wei_a = res_a['wei'] + VWi[i]['wei']

    # case b: iをつかわないときー
    res_b = all_search(i-1, w)
    val_b = res_b['val']
    wei_b = res_b['wei']

    if wei_a > w:
        return {'val': val_b, 'wei': wei_b}
    else:
        return max([{'val': val_a, 'wei': wei_a}, {'val': val_b, 'wei': wei_b}], key=lambda ele: ele['val'])


# 漸化式
DP = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for w in range(1, W+1):
        val = VWi[i-1]['val']
        wei = VWi[i-1]['wei']

        if w - wei >= 0:
            tukau = DP[i-1][w-wei] + val
            tukawanai = DP[i-1][w]
            DP[i][w] = max(tukau, tukawanai)
        else:
            DP[i][w] = DP[i-1][w]
# print(DP[-1][-1])


# メモ化
checked = [[False if i != 0 and w != 0 else True for w in range(W+1)] for i in range(N+1)]
results = [[0 for w in range(W+1)] for i in range(N+1)]
def memo_search(i,w):
    if i < 0:
        return 0
    if checked[i][w]:
        return results[i][w]

    # case a: iを使うときー
    if w >= VWi[i-1]['wei']:
        tukau = memo_search(i-1, w - VWi[i-1]['wei']) + VWi[i-1]['val']
    else:
        tukau = 0

    # case b: iをつかわないときー
    tukawanai = memo_search(i-1, w)

    ans = max(tukau, tukawanai)
    checked[i][w] = True
    results[i][w] = ans

    return ans
print(memo_search(N, W))



