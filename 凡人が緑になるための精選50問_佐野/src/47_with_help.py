'''
https://atcoder.jp/contests/abc185/tasks/abc185_f

完全に写経．

'''

class SegTree:
    def __init__(self, x_list, init, segfunc):
        self.init = init
        self.segfunc = segfunc
        self.height = len(x_list).bit_length() + 1
        self.tree = [init] * (2**self.height)
        self.num = 2**(self.height-1)
        for index, x in enumerate(x_list):
            self.tree[2**(self.height-1) + index] = x
        for i in range(2**(self.height-1)-1, 0, -1):
            self.tree[i] = segfunc(self.tree[2*i], self.tree[2*i+1])

    def select(self, k):
        return self.tree[k+self.num]

    def update(self, k,x):
        i = k + self.num
        self.tree[i] = x
        while i > 1:
            if i%2 == 0:
                self.tree[i//2] = self.segfunc(self.tree[i], self.tree[i+1])
            else:
                self.tree[i//2] = self.segfunc(self.tree[i-1], self.tree[i])

            i //= 2

    def query(self, l, r):
        result = self.init
        l += self.num
        r += self.num + 1

        while l < r:
            if l%2==1:
                result = self.segfunc(result, self.tree[l])
                l+=1
            if r%2==1:
                result = self.segfunc(result, self.tree[r-1])
            l //= 2
            r //= 2

        return result 


N,Q = map(int, input().split())
A = list(map(int,input().split()))
seg = SegTree(A,0, lambda a,b: a^b)

for i in range(Q):
    T,X,Y = map(int, input().split())
    if T == 1:
        X -= 1
        seg.update(X,seg.select(X) ^ Y)
    else:
        X -= 1
        Y -= 1
        print(seg.query(X,Y))