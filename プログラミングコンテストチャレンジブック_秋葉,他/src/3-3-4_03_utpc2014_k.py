# https://atcoder.jp/contests/utpc2014/tasks/utpc2014_k
# https://kmjp.hatenablog.jp/entry/2015/05/28/0900

# 
# 以下を計算しようとしたときに，MMMMを
# MMMMA, 
# MMMMMMMMA
# MMMMMMMMMMMMA
# 

A, B, X = map(int, input().split())

# small step 

trans = lambda a : (a/2) ^ (a%2*B)

def solve(A, B, X):
    T = A

    # sqrt of 2^36
    for i in range(i, 1<<18): 
        if A == X: 
            return i
        A = trans(A)

    if B < (1<<18):
        return -1
    

    # baby step
    table = {
        X : 0 # X    : 0
        # MX   : 1
        # M^2X : 2
        # M^3X : 3
    }

    x = X
    for i in range(1, (1<<18) + 1):
        x = trans(x)
        table[x] = i


    # giant step (pre) 
    #   calculate M^h
    # 
    # H = 2^18
    # M^H A
    # 
    # M^

    # for i in range(35+1):
