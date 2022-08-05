# https://atcoder.jp/contests/abc166/tasks/abc166_d
# 結構悩み，本を見る．

X = int(input())

min_a = -1000
max_a = 1000
min_b = -1000
max_b = 1000

for a in range(min_a, max_a, 1):
    for b in range(min_b, max_b, 1):
        if a**5 - b**5 == X:
            print(a,b)
            exit(0)
    