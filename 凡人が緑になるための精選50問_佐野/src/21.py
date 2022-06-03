# https://atcoder.jp/contests/abc195/tasks/abc195_b
# あまりエレガントな回答ではない．

A, B, W = map(int, input().split())

W = W * 1000

ans='UNSATISFIABLE'

# Find max_num
a = W // A
remain_a = W - A*a
ans_max_num = None

if remain_a == 0:
    ans_max_num = a   
else:
    for a in range(W//A, 1, -1):
        b = 1
        while W >= A*a + A*b:
            remain = (W - a * A)
            if remain / b >= A and remain / b <= B:
                ans_max_num = a + b
                break
            else:
                b = b + 1
        if ans_max_num:
            break

b = W // B
remain_B = W - B*b
ans_min_num = None

if remain_B == 0:
    ans_min_num = b
else:
    for b in range(W // B,1,-1):
        a = 1
        while W >= A*a + B*b:
            remain = (W - b * B)
            if remain / a >= A and remain / a <=B:
                ans_min_num = a+b
                break
            else:
                a = a + 1
        if ans_min_num:
            break

if ans_min_num is None:
    print(ans)
else:
    print(ans_min_num, ans_max_num)

