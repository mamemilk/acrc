'''
https://atcoder.jp/contests/abc156/tasks/abc156_d

解説見ました．
完全に写経．

'''

n, a, b = map(int, input().split())

mod = 10** 9 + 7

def nCr_mod( n, r, mod): 
    numerator = 1 
    for i in range(n-r + 1, n+1): 
        numerator*= i 
        numerator%= mod 
        
    denominator = 1
    for i in range(1, r + 1):
         denominator*= i 
         denominator%= mod
    
    denominator_inv = pow(denominator,-1,mod) 
    return numerator* denominator_inv % mod
         
ans = pow(2,n,mod) - 1 - nCr_mod( n, a, mod) - nCr_mod( n, b, mod) 
ans%= mod 

print(ans)
