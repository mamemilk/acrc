# https://atcoder.jp/contests/abc203/tasks/abc203_c

"""
K=0でスタートして，各街で進めるかどうかを判別した実装だと，計算時間が間に合わない．
カンニング．

now_village = 0
now_village += K
を最初にやっておいて，計算時間を節約している．
"""
N, K = map(int, input().split())

AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a,b))

AB.sort(key=lambda ele:ele[0])
#print('debug',AB)
nv = 0
nv += K
for a,b in AB:
    if a <= nv:
        nv += b
    else:
        break

print(nv)



# N, K = map(int, input().split())

# AB = []
# for i in range(N):
#     a, b = map(int, input().split())
#     AB.append((a,b))

# AB.sort(key=lambda ele:ele[0])
# #print('debug',AB)
# i = 0
# while len(AB) > 0:
#     if K == 0:
#         break

#     a, b = AB.pop(0)

#     #print('debug', i, K, a, b)
#     if K >= (a - i): # can reach to village a
#         K = K - (a - i) + b
#         i = a
#         if len(AB) == 0:
#             i += K
#             K = 0
#     else:
#         i += K
#         K = 0

# print(i)
