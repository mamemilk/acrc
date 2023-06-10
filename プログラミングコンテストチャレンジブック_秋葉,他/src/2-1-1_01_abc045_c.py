# https://atcoder.jp/contests/arc061/tasks/arc061_a

S = input()
P_len = len(S) - 1
P_max = 1<<P_len
P = 0

ans = 0
while P < P_max:
    res = S[0]
    for index, s in enumerate(S[1:]):
        if (P>>index) & 0x1:
            res += "+"

        res += s

    ans += eval(res)
    #print(res)
    P += 1

print(ans)