# https://atcoder.jp/contests/arc006/tasks/arc006_3

N = int(input())
Wi = []
for i in range(N):
    Wi.append(int(input()))

arr = []

for w in Wi:
    candids = list(filter(lambda ele: ele[1] >= w, arr))
    if len(candids) == 0:
        arr.append((len(arr), w))
    else:
        candid = min(candids, key=lambda ele: ele[1])
        arr[candid[0]] = (candid[0], w)

print(len(arr))
