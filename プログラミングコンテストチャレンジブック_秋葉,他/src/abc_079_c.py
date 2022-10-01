# https://atcoder.jp/contests/abc079/tasks/abc079_c

S = input()
P_max = 1<<3
P = 0


ans = 0
while P < P_max:
    res = S[0]
    for index, s in enumerate(S[1:]):
        if (P>>index) & 0x1:
            res += "+"
        else:
            res += "-"
        res += s

    if eval(res) == 7:
        print('{}={}'.format(res, 7))
        break

    P += 1
