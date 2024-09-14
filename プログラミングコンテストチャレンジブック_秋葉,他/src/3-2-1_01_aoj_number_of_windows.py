# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C&lang=jp
# 
# 

N, _ = map(int, input().split())

ai = [*map(int, input().split())]
xi = [*map(int, input().split())]

def analyze(x):
    l = 0
    r = 0
    sum = 0 
    ans = 0
    while l < N:
        while r < N and sum + ai[r] <= x:
            sum += ai[r]
            r += 1
        if l == r: # sumが大きくて，rを動かせず, lをインクリメント．rはlに戻す
            l += 1
            r = l
        else:
            ans += r - l
            sum -= ai[l]
            l += 1
    return ans

    # 
    # while sum + ai[r] <= xを避けようとが
    # 
    # l = 0
    # r = 0
    # sum = 0 
    # ans = 0
    # while r < len(ai) :
    #     # print(l, r, sum, sum <= x)

    #     if sum <= x:
    #         ans += 1

    #         if l == r:
    #             r += 1 
    #             if r == len(ai):
    #                 break
    #             else:
    #                 sum += ai[r]
    #         else: 
    #             sum -= ai[l]
    #             l += 1

    #     elif sum > x:
    #         sum -= ai[l]
    #         l += 1

    # return ans

for x in xi:
    print(analyze(x))