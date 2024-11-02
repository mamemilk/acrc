# https://atcoder.jp/contests/arc088/tasks/arc088_b
# 
# S sequence  'b 00101010
#             'b 00100000 
#             'b 00001000
#             'b 00000010
# 

S = input()
N = len(S)

ans = N + 1
for k, s in enumerate(S):
    if k == N-1:
        continue

    if s != S[k+1]:
        ans = min(ans, max(k+1, N-(k+1)))
        # print(ans)
print(ans)
