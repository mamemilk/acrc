#https://atcoder.jp/contests/abc201/tasks/abc201_b
# 八木さんの回答が，早そう.
# https://github.com/syagi/atcoder_training/blob/main/06_abc201b.py

N = int(input())
ST = []

for i in range(N):
    s, t = input().split()
    t = int(t)
    ST.append((s,t))

ST.sort(key=lambda a:a[1])
print(ST[-2][0])
