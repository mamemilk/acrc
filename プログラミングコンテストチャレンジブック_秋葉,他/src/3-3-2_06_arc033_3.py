# https://atcoder.jp/contests/arc033/tasks/arc033_3
# 
# BIT上で固定回数の2分探索をしたいのだが、REが取れない。号泣。1時間ほど吸い取られたのでギブアップ。
# 二分探索でやる。
# 

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

'''
bit = BinaryIndexedTree(size=16)
# bit.update(1,1)
bit.update(2,1)
bit.update(3,1)
bit.update(5,1)
bit.update(7,1)
bit.update(12,1)

bit.lower_bound(0)
bit.lower_bound(2)
bit.lower_bound(3)
bit.lower_bound(4)
bit.lower_bound(5)
# bit.lower_bound(9)

# exit(-1)
'''

Q = int(input())
bit = BinaryIndexedTree(size=200_000)
for _ in range(Q):
    t,x = map(int, input().split())

    if t == 1:
        bit.update(x, 1)
    else:
        l, r = 1, 200_000
        while l < r:
            m = (l + r) // 2
            if bit.query(m) >= x:
                r = m
            else:
                l = m + 1
        print(l)
        bit.update(l, -1)



        # ans = bit.lower_bound(x)
        # bit.update(ans, -1)
        # print(ans)