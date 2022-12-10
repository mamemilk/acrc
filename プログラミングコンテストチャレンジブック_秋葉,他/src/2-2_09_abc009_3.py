# https://atcoder.jp/contests/abc009/tasks/abc009_3
# 
# Sを並び替えた文字を順に使う(t)
# tの不一致数 + 後ろの最小の不一致数が Kを下回ったらtを1文字育てる．
# これを繰り返す．

N, K = map(int, input().split())
S = input()

Ss = sorted(S)
rest = list(S)

t = ''
count_t = 0

def min_count(A, B): # A is original string, B is candidate array
    tmp = [ele for ele in B]
    count = 0
    for c in A:
        if c in tmp:
            tmp.remove(c)
        else:
            count += 1
    return count

def diff_count(A,B): # A, B string
    count = 0
    for a,b in zip(A,B):
        if a != b:
            count += 1    
    return count

index = 0

while True:
    # print('before', rest)
    count_a = diff_count(S[0:len(t)], t)
    count_b = min_count(S[len(t):], rest)
    
    if count_a + count_b >= K or index >= len(Ss):
        break

    #print(t, count_a, count_b, index)

    t += Ss[index]
    rest.remove(Ss[index])
    index += 1


print(t + ''.join(rest))