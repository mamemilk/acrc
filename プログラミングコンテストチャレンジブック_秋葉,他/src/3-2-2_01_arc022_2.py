# https://atcoder.jp/contests/arc022/tasks/arc022_2

N = int(input())
ai = [*map(int, input().split())]


def tle_case():
    ans = 0
    flavors = []
    r = 0 
    while r < N:
        ar = ai[r]
        if ar in flavors:
            flavors = flavors[flavors.index(ar)+1:]
        flavors.append(ar)
        ans = max(ans, len(flavors))    
        r += 1

    print(ans)

def ok_case():
    flavors = [0] * (100000 + 1)

    l = 0
    ans = 0
    for r in range(N):
        # print(r)
        ar = ai[r]
        flavors[ar] += 1
        while flavors[ar] >= 2:
            flavors[ai[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
    print(ans)

ok_case()