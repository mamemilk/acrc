# https://atcoder.jp/contests/abc199/tasks/abc199_c
# 演算時間でパスせず．愚直な実装はだめなようだ．
# 本をカンニングしてしまった．
# 配列の前後の入れ替えのコストが高いのが，いまいち納得できておらず．
# 
# 0,1,2,3,  4,5,6,7
# 0,4,2,3   1,5,6,7
# 
# 鳥海さんの実装が，エレガント．
#             a = (a -1 + N) % (N * 2)
#             b = (b -1 + N) % (N * 2)


N = int(input())
S = input()
Q = int(input())

Queries = []
for i in range(Q):
    t,a,b = map(int, input().split())
    a -= 1
    b -= 1
    Queries.append((t,a,b))

S_pre = list(range(2*N))
is_flip = False

for t,a,b in Queries:
    if t == 1:
        if is_flip:
            a = a + N if a < N else a - N
            b = b + N if b < N else b - N
            S_pre[a],S_pre[b] = S_pre[b], S_pre[a]
        else:
            S_pre[a],S_pre[b] = S_pre[b], S_pre[a]
    else: # t==2
        #S_pre = S_pre[N:2*N] + S_pre[0:N]
        is_flip ^= True # xorで反転

if is_flip:
    S_pre = S_pre[N:2*N] + S_pre[0:N]

for i in S_pre:
    print(S[i], end='')
print('')

# flip = False

# for t,a,b in Queries:
    
#     if t == 1:
#         if not flip:
#             if b == N*2-1:
#                 S = S[:a] + S[b] + S[a+1:b] + S[a]
#             else:
#                 S = S[:a] + S[b] + S[a+1:b] + S[a] + S[b+1:]
#         else :
#             if b == N*2-1:
#                 S = S[:a] + S[b] + S[a+1:b] + S[a]
#             else:
#                 S = S[:a] + S[b] + S[a+1:b] + S[a] + S[b+1:]

#     elif t == 2:
#         former = S[0:N]
#         latter = S[N:]
#         S = latter + former
