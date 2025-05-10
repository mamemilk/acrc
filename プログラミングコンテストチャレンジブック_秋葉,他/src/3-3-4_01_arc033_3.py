# https://atcoder.jp/contests/arc033/tasks/arc033_3
# 平方分割、SQRT(N)で分割するのが計算量最小

class Heiho():
    def __init__(self, n=200_000):
        self.D = int(n ** 0.5)
        self.S = [[] for _ in range((n + self.D-1) // self.D)]

    def add(self, x):
        index = x // self.D
        for i, xi in enumerate(self.S[index]):
            if x <= xi:
                self.S[index].insert(i, x)
                return
        self.S[index].append(x)
        return

    def query(self, num):        
        for s in self.S:
            if num <= len(s):
                ans = s.pop(num-1)
                return ans
            else:
                num -= len(s)
        assert True, "Error: num is too large"

Q = int(input())

H = Heiho()
for _ in range(Q):
    T, X = map(int, input().split())
    if T == 1: # add Xi 
        H.add(X)
        # print("Add", H.S)
    else: # query
        print(H.query(X))
        # print("Query", H.S)