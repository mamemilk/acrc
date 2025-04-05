# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_G&lang=jp

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

class RangeAddQuery:
    def __init__(self, size):
        self.bit0 = BinaryIndexedTree(size)
        self.bit1 = BinaryIndexedTree(size)

    def range_add(self, left, right, value):
        self.bit0.update(left, -value * (left - 1))
        self.bit0.update(right + 1, value * right)
        self.bit1.update(left, value)
        self.bit1.update(right + 1, -value)

    def query(self, index):
        return self.bit0.query(index) + self.bit1.query(index) * index

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

n, q = map(int, input().split())

raq = RangeAddQuery(n)

for _ in range(q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        s, t = query[1:]
        print(raq.range_query(s, t))
    else:
        s, t, x = query[1:]
        raq.range_add(s, t, x)    





