# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D&lang=jp
# 
# BIT
# 
# length == 8
#                                    [1,8]     
#                [1,4] 
#      [1,2]               [5,6]        
#  [1]       [3]       [5]       [7]   
# 
#i  1    2    3    4    5    6    7    8

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

# bit = BinaryIndexedTree(size=10)
# bit.update(10,1)
# print(bit.query(10))
# print(bit.query(9))

# bit.update(10,1)
# print(bit.query(10))
# print(bit.query(9))

# bit.update(9,1)
# print(bit.query(10))
# print(bit.query(9))

size = int(input())
Ai = list(map(int, input().split()))

# 座標圧縮
AiMap = {a: index+1 for index, a in enumerate(sorted(Ai))}

bit = BinaryIndexedTree(size)

ans = 0
for a in Ai:
    apost = AiMap[a]
    bit.update(apost, 1)
    ans += bit.range_query(apost+1,size)

print(ans)
