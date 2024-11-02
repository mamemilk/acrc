# https://atcoder.jp/contests/abc023/tasks/abc023_d

# 横軸を秒，縦軸を得点としたときに

N = int(input())
HS = []
for _ in range(N):
    h, s = map(int, input().split())
    HS.append((h,s))

# ペナルティの上限値
x = sorted(map(lambda hs : hs[0] + hs[1] * (len(HS)-1), HS))[-1]

left, right = 0, x

while left + 1 < right:
    half = (left + right) // 2
    # 制限時間リスト，**秒までに打たないとNGの，**が入ってる
    candid = sorted(map(lambda hs: (half-hs[0]) // hs[1], HS))

    # print(left, half, right)

    # 
    is_ok = True
    for s in range(N):
        if candid[s] < s:
            is_ok = False
            break
    
    if is_ok: 
        left, right = left, half
    else : 
        left, right = half, right
        
print(right)
