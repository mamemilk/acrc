# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E&lang=ja
# ax + by = gcd(a,b)
# 拡張ユークリッド互除法，で検索して以下ページを見て実装した．
# https://tbasic.org/reference/old/ExEuclid.html
# https://zenn.dev/senk/articles/8a230c83b5a614d175db
# 

a, b = map(int, input().split())
    
def ext_euclid(a,b):
    if b == 0:
        return (1,0)
    d = ext_euclid(b, a%b)
    q = a // b
    return (d[1], d[0]-q*d[1])

ans = ext_euclid(a,b)
print(*ans)