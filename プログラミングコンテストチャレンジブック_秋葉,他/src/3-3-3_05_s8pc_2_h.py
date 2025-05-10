# https://atcoder.jp/contests/s8pc-2/tasks/s8pc_2_h
# 
# 遅延評価Segment Treeで反転の有無を覚える。

class LazySegmentTree:
    def __init__(self, n):
        self.size = 1 << (n - 1).bit_length()
        self.tree = [0] * (2*self.size-1)
        self.lazy = [0] * (2*self.size-1)
    
    def propagate(self,i,l,r):
        if self.lazy[i]:
            self.tree[i] = (r-l)-self.tree[i]
            if r-l > 1:
                self.lazy[i*2+1] ^= self.lazy[i]
                self.lazy[i*2+2] ^= self.lazy[i]
            self.lazy[i]=0

    def update_range(self, s, t, i=0, l=0,r=None):
        if r==None:
            r=self.size
        self.propagate(i,l,r)

        if t <= l or s >= r:
            return
        if s <= l and t >=r:
            self.lazy[i]=1
            self.propagate(i,l,r)
        else:
            m = (l+r)//2
            self.update_range(s, t, i*2+1, l, m)
            self.update_range(s, t, i*2+2, m ,r)
            self.tree[i] = self.tree[i*2+1]+self.tree[i*2+2]

    def query_range(self, s, t, i=0, l=0, r=None):
        if r==None:
            r=self.size
        self.propagate(i,l,r)
        if t <= l or s >= r:
            return 0
        if s <= l and t >= r:
            return self.tree[i]
        m = (l+r)//2
        count_left = self.query_range(s, t, 2*i+1, l, m)
        count_right = self.query_range(s, t, 2*i+2, m, r)
        return count_left + count_right
    

n, Q = map(int, input().split())

seg = LazySegmentTree(n)
for _ in range(Q):
    q, l, r = map(int, input().split())

    if q == 1:
        seg.update_range(l, r)
    else:
        print(seg.query_range(l, r))

        