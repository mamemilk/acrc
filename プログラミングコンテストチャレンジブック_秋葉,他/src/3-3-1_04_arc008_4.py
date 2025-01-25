# https://atcoder.jp/contests/arc008/tasks/arc008_4

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

affine = lambda x, y: [x[0] * y[0], x[1] * y[0] + y[1]]

N, M = map(int, input().split())
used = dict()
comp = []
for _ in range(M):
    # p = box index, there're duplicates
    p, a, b = map(float, input().split())
    p = int(p) - 1
    comp.append([p, a, b])
    used[p] = True

comp_keys = used.keys()
forward_map = dict([[p,index] for index, p in enumerate(comp_keys)])
print(
    forward_map
)
backward_map = dict([[index, p] for index, p in enumerate(comp_keys)])

rmq = RMQ(len(comp_keys), op=affine, initial_value=[1, 0])
maxim = 1
minimum = 1
for c in comp:
    p, a, b = c
    print(p)
    p_mapped = forward_map[p]
    rmq.update(p_mapped, [a, b])
    res = rmq.query(0, len(comp_keys))
    maxim = max(maxim, res)
    minimum = min(minimum, res)

print(minimum)
print(maxim)

