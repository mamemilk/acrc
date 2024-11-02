# https://atcoder.jp/contests/arc075/tasks/arc075_c
# 
# 

N, K = map(int, input().split())
Ai = [int(input())-K for _ in range(N)]

class binary_index_tree:
  def __init__(self, n):
    self.n = n
    self.data = [0] * (n + 1)
    self.el = [0] * (n + 1)

  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s

  def add(self, i, x):
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i

  def get(self, i, j = None):
    if j is None:
      return self.el[i]
    return self.sum(j) - self.sum(i)

  def lowerbound(self, s):
    x = 0
    y = 0
    for i in range(self.n.bit_length(), -1, -1):
      k = x + (1 << i)
      if k <= self.n and (y + self.data[k] < s):
        y += self.data[k]
        x += 1 << i
    return x + 1
  

for i in range(1, N):
  Ai[i] += Ai[i-1]
 
Ai.append(0)   

d = []
d.append((Ai[-1-1],N+1))
for i in range(N):
  d.append((Ai[i-1],i+1)) 
d.sort()

ans = 0 
fw = binary_index_tree(N+1)

for x,ind in d:
  fw.add(ind,1)
  ans += fw.sum(ind-1)
print(ans)
    