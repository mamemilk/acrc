# https://atcoder.jp/contests/arc037/tasks/arc037_b

# 閉路判定
# - DFS
#   訪問済みの頂点を再度訪問したときに閉路存在．
# 
# - UnionFind
#   a,bの辺を張るときに，すでに同じグループなら閉路が存在．
# 


N, M = map(int, input().split())

UV = []
for m in range(M):
    u, v = map(int, input().split())
    UV.append((u,v))


class UnionFind:
    def __init__(self, n): 
        self.n = n 
        self.parent_size =[- 1]* n
        self.heiro = [False] * n
        
    def merge(self, a, b): 
        x, y = self. leader(a), self. leader(b) 
        if x == y: 
            self.heiro[x] = True
            return True
        if abs(self.parent_size[x]) < abs( self.parent_size[y]): 
            x, y = y, x    
        self.parent_size[x] += self. parent_size[y] 
        self.parent_size[y]= x 
        return False
    
    def same(self, a, b): 
        return self. leader( a) == self. leader( b) 
        
    def leader(self, a): 
        if self.parent_size[ a]< 0: 
            return a 
        self.parent_size[ a]= self. leader(self. parent_size[ a]) 
        return self. parent_size[ a] 
        
    def size( self, a): 
        return abs(self.parent_size[ self.leader( a)]) 
        
    def groups( self): 
        result =[[] for _ in range( self. n)] 
        for i in range( self. n): 
            result[ self. leader( i)]. append( i)     
        return [r for r in result if r != []]

    def open_groups( self): 
        result =[[] for _ in range( self. n)] 
        for i in range( self. n): 
            if self.heiro[self.leader(i)]:
                pass
            else:
                result[self.leader(i)].append(i)     
        return [r for r in result if r != []]

Uni = UnionFind(N)

for u,v in UV:
    Uni.merge(u-1,v-1)

print(len(Uni.open_groups()))
