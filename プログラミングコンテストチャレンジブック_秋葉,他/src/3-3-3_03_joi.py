# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_G&lang=jp
# 
#　鳥海さんのソースのコメントの、
#　　 A[i] と min(A[i], A[i+1]) の個数の差分を計算する
# でようやく理解。


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


n, q = map(int, input().split())

employee = [int(input()) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

tokuten_set = set(employee + [query[2] for query in queries if query[0] == 2])
tokuten2comp = {tokuten: i+1 for i, tokuten in enumerate(sorted(tokuten_set, reverse=True))}

bit = BinaryIndexedTree(len(tokuten_set))
for i in range(n):
    bit.update(tokuten2comp[employee[i]], 1)
    if i < n - 1:
        bit.update(tokuten2comp[min(employee[i], employee[i+1])], -1)

for query in queries:
    if query[0] == 1:
        threshold, = query[1:]
        print(bit.query(tokuten2comp[threshold]))

        # print(st.query_min(s, t+1))
    else:
        emp, toku = query[1:]
        emp -= 1

        bit.update(tokuten2comp[employee[emp]], -1)
        bit.update(tokuten2comp[toku], 1)
        if emp > 0:
            bit.update(tokuten2comp[min(employee[emp-1], employee[emp-1])], 1)
            bit.update(tokuten2comp[min(toku,            employee[emp-1])], -1)
        if emp < n-1:
            bit.update(tokuten2comp[min(employee[emp], employee[emp+1])], 1)
            bit.update(tokuten2comp[min(toku,            employee[emp+1])], -1)
        employee[emp] = toku

