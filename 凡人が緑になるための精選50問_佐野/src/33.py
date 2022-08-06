# https://atcoder.jp/contests/abc177/tasks/abc177_d
# 
# かなり苦労した．
# 
# 友達グループA 1 2 3 4 
#            B 5 6 
#            C 7 8 9 
# この場合，同じグループに友達が居ないグループの分け方は，4グループ．
# 最大のグループの要素数が答えになる．


# friendsをsetでもつ以下実装で，TLE 2件，WA 9件．TLEはわかるが，WAがなんでかがわかってない．
'''
N, M = map(int, input().split())

friends_set_by_id = list(range(N))

for m in range(M):
    a,b = map(int, input().split())
    if type(friends_set_by_id[a-1]) is int and type(friends_set_by_id[b-1]) is int:
        friends_set_by_id[a-1] = set([a,b])
        friends_set_by_id[b-1] = friends_set_by_id[a-1]
    elif type(friends_set_by_id[b-1]) is int:
        friends_set_by_id[a-1].add(b)
        friends_set_by_id[b-1] = friends_set_by_id[a-1]
    elif type(friends_set_by_id[a-1]) is int:
        friends_set_by_id[b-1].add(a)
        friends_set_by_id[a-1] = friends_set_by_id[b-1]
    else:
        tmp = friends_set_by_id[a-1] | friends_set_by_id[b-1] 
        friends_set_by_id[a-1] = tmp
        friends_set_by_id[b-1] = tmp
#print(friends_set_by_id)

print(max([len(ele) if type(ele) is not int else 1 for ele in friends_set_by_id]))
'''

# テキストをカンニングしました．

class UnionFind: 
    def __init__( self, n): 
        self.n = n 
        self.parent_size =[- 1]* n 
        
    def merge( self, a, b): 
        x, y = self. leader( a), self. leader( b) 
        if x == y: 
            return 
        if abs( self.parent_size[ x])< abs( self.parent_size[ y]): 
            x, y = y, x    
        self. parent_size[ x] += self. parent_size[ y] 
        self. parent_size[ y]= x 
        return 
    
    def same( self, a, b): 
        return self. leader( a) == self. leader( b) 
        
    def leader( self, a): 
        if self. parent_size[ a]< 0: 
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

N, M = map(int, input().split())

Uni = UnionFind(N)

for i in range(M):
    A,B = map(lambda a: int(a)-1, input().split())
    Uni.merge(A,B)

#print(Uni.groups())

print(max([len(g) for g in Uni.groups()]))

