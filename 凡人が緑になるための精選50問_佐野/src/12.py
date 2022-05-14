# https://atcoder.jp/contests/abc148/tasks/abc148_c
def gcd(x, y):
   while y:
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

A, B = map(int, input().split())

print(lcm(A,B))