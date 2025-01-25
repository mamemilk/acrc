# https://atcoder.jp/contests/jag2013summer-day2/tasks/icpc2013summer_day2_g

import math


class RMQ:
    def __init__(self, length, op=max, initial_value=float('inf')):
        self.initial_value = initial_value
        self.op = op
        self.length = 1<<(length-1).bit_length()
        self.tree = [self.initial_value] * (2 * self.length - 1)

    def update(self, k, ax):
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

mod = 10 ** 9 + 7

N, Q = map(int, input().split())
Pi = [*map(int, input().split())]

addmod = lambda a,b : (a+b)%mod
rmq_lcm = RMQ(N, op=math.lcm, initial_value=1)
rmq_addmod = RMQ(N, op=addmod, initial_value=0)

for x in range(N):
    s, t, y = 0, 0, x
    while True:
        y = Pi[y-1]
        s += y
        t += 1
        if y == x:
            break
    rmq_lcm.update(x, t)
    s *= pow(t, -1, mod)
    s %= mod
    rmq_addmod.update(x, s)

for _ in range(Q):
    l, r = map(int, input().split())
    t = rmq_lcm.query(l-1, r)
    s = rmq_addmod.query(l-1, r)

    print((s*t)%mod)