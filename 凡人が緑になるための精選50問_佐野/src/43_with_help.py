'''
https://atcoder.jp/contests/abc174/tasks/abc174_c

解説見ました．

鳥海さんは，0~Kのフラグで循環を検知．
テキストは，"鳩ノ巣原理"でやっている．

'''

K = int(input())

amari = 0

for i in range(1, K+1):
    amari = amari * 10 + 7

    if amari % K == 0:
        print(i)
        exit(0)

    amari %= K 
print(-1)
