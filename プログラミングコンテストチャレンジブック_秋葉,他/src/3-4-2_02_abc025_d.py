# https://atcoder.jp/contests/abc025/tasks/abc025_d
#
# dp[i], bitDPで1<<25の要素数，その時点で矛盾なく置かれている配置の総数
# f(i,j) : iの第jビット目が0で，状態iから新たに数をjマスにおいても矛盾しない場合に1をそれ以外は0を返す

# DPを 1<<25にするとTLE． 
# DPを配列ではなく辞書で持つところは，どなたかの回答をカンニン．．．参考にさせていただいた．

x = [list(map(int, input().split())) for _ in range(5)]
x = x[0] + x[1] + x[2] + x[3] + x[4]

fixeds_dict = {} # 数字が入っているマス用，数字がkeyで，マスのインデックスがvalue, 
unfixeds = [] # 数字が入ってないマスのインデックス
for j in range(25):
    if x[j]:
        fixeds_dict[x[j]] = [j]
    else:
        unfixeds.append(j)

dp = {}
dp[0] = 1
dp[(1<<25) - 1] = 0

# iが状態，jはマスのインデックス
for i in range((1<<25)):
    if i not in dp:
        continue
    # 次に埋める数．1から順番に埋めていくが，状態iから求まる次の数nを求める．
    n = sum(i >> j & 1 for j in range(25)) + 1

    # nがfixならそのマスだけが候補，層でなければ，空いてるマスが候補
    candids = fixeds_dict[n] if n in fixeds_dict else unfixeds

    for j in candids:
        # nをjマスに入れていいかチェック．状態iがjを埋めていないか，jマスが空いているかnが入っているか
        if i >> j & 1 == 0 and x[j] in [0, n]:
            if not (
                0 < j % 5 < 4 and i >> (j - 1) & 1 != i >> (j + 1) & 1 or  # 横方向 解説スライドの片方埋まってて片方埋まってない
                4 < j < 20    and i >> (j - 5) & 1 != i >> (j + 5) & 1     # 縦方向 
                ):

                if i | (1<<j) not in dp:
                    dp[i | (1<<j)] = dp[i]
                else:
                    dp[i | (1<<j)] += dp[i]
                    dp[i | (1<<j)] %= 10 ** 9 + 7

print(dp[(1<<25) - 1])