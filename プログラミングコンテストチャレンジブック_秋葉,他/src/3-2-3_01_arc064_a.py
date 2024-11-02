# https://atcoder.jp/contests/arc064/tasks/arc064_a

# 左端，a, b, cとならんでた場合，aを減らしても b + cに影響与えない．
# bを一番小さくできるようにするのが最適で，貪欲に左から求めて行けばよいと思われる．
# a > xのときは，aをxにする必要あり．

N, x = map(int, input().split())
Ai = [*map(int, input().split())]

cnt = 0

prev = Ai[0]
if prev > x:
    cnt += prev - x
    prev = x

for curr in Ai[1:]:
    if prev + curr > x:
        d = (prev + curr - x)
        cnt += d
        prev = curr - d

print(cnt)