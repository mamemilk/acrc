# https://atcoder.jp/contests/wupc2nd/tasks/wupc_07

import math

# 1 indexed 
class BinaryIndexedTree:
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.bit[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.bit[index]
            index -= index & -index
        return result

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)
    
    def lower_bound(self, value):
        # if value > self.query(self.size):
        #     return self.size + 1

        npower = int(math.log2(self.size-1))
        index = 2**(npower)
        # print(index)

        for n in range(npower, 0, -1):
            index_post = min(index, self.size)
            # print("n, index, value, bit=", n, index, value, self.bit[index_post])
            if self.bit[index] >= value:
                index = index - 2 ** (n-1)
            else: 
                value = value - self.bit[index]
                index = index + 2 ** (n-1)

        # print("n, index, value, bit=", 0, index, value, self.bit[index_post])
        
        index_post = min(index, self.size)
        if self.bit[index_post] < value:
            index += 1

        # print("ans:",index)
        return index 
    

N, M, H = map(int, input().split())

A = list(map(int, input().split()))

bit = BinaryIndexedTree(size=100_000)
for index, a in enumerate(A):
    bit.update(index+1, a)
# length = len(A)

# for _ in range(M):
for line in [input() for _ in range(M)]:
    q = line.split()
    ope, arg = q[0], int(q[1])  

    if ope == "add":
        A.append(arg)
        # length += 1
        bit.update(len(A)+1, arg)
    else: # challenge
        if bit.query(len(A)) <= arg - H: 
            print("miss")
        else:
            l, r = 1, len(A)
            while l < r:
                m = (l+r) // 2
                # print("m  ", m, bit.query(m))
                if bit.query(m) > arg - H:
                    r = m
                else:
                    l = m + 1
                # print(l,m,r, arg-H, bit.query(m))

            h = bit.query(l)
            if h < arg + H and h < bit.query(len(A)):
                print("stop")
            else:
                print("go")
                bit.update(l, -A[l-1])
                
