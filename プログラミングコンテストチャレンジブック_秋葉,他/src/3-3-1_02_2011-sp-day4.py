# https://www2.ioi-jp.org/camp/2011/2011-sp-tasks/2011-sp-day4.pdf
#
# Chose which NOT to pick. 
# Find increasing sequence with maximum total weight. 

class RMQ:
    def __init__(self, length, op=max, initial_value=float('inf')):
        self.initial_value = initial_value
        self.op = op
        self.length = 1<<(length-1).bit_length()
        self.tree = [self.initial_value] * (2 * self.length - 1)

    def update(self, k, a):
        k += self.length - 1  # when k=0, then first leaf is [0+n-1]
        self.tree[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.tree[k] = self.op(self.tree[k * 2 + 1], self.tree[k * 2 + 2])

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
        return self.op(vl, vr)



n = int(input())

A = [int(input()) for _ in range(n)]
B = [int(input())-1 for _ in range(n)]

rmq = RMQ(n, op=max, initial_value=0)
for bi in B:
    t = rmq.query(0, bi+1) + A[bi]
    rmq.update(bi, t)

ans = (sum(A) - rmq.query(0, n+1)) * 2 
print(ans)


