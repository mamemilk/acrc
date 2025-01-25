# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A&lang=jp
#
# when n=8 
# 
#         0 
#    1          2
#  3   4     5     6
# 7 8 9 10 11 12 13 14

class RMQ:
    def __init__(self, length, initial_value=float('inf')):
        self.initial_value = initial_value
        self.length = 1<<(length-1).bit_length()
        self.tree = [self.initial_value] * (2 * self.length - 1)

    def update(self, k, a):
        k += self.length - 1  # when k=0, then first leaf is [0+n-1]
        self.tree[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.tree[k] = min(self.tree[k * 2 + 1], self.tree[k * 2 + 2])

    """
    Queries the segment tree for the minimum value in the range [a, b).

    Args:
        a (int): The start of the range (inclusive).
        b (int): The end of the range (exclusive).
        k (int, optional): The index of the current node in the segment tree. Defaults to 0.
        l (int, optional): The left boundary of the current segment. Defaults to 0.
        r (int, optional): The rigself.initial_valueht boundary of the current segment. Defaults to None.

    Returns:
        float: The minimum value in the range [a, b).
    """
    def query(self, a, b, k=0, l=0, r=None):
        if r is None:
            r = self.length
        if r <= a or b <= l:
            return self.initial_value
        if a <= l and r <= b:
            return self.tree[k]
        vl = self.query(a, b, k * 2 + 1, l, (l + r) // 2)
        vr = self.query(a, b, k * 2 + 2, (l + r) // 2, r)
        return min(vl, vr)



n, q = map(int, input().split())
rmq = RMQ(n, 2**31-1)
for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        rmq.update(x, y)
    else:
        print(rmq.query(x, y+1))


