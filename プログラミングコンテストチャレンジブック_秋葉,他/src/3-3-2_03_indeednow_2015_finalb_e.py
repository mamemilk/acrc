# https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_e
# 

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

size = int(input())
Ai = list(map(int, input().split()))

# 座標圧縮
AiMap = {a: index+1 for index, a in enumerate(sorted(Ai))}

bit = BinaryIndexedTree(size)

ans = 0
for a in Ai:
    apost = AiMap[a]

    if bit.range_query(apost, apost) == 1:
        print(-1)
        exit(0)

    bit.update(apost, 1)
    ans += a * bit.range_query(apost+1,size)

print(ans)
