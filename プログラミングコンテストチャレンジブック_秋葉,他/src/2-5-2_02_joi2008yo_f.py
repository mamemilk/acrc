# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f

n, k = map(int, input().split())
cost = [[float("inf") for _ in range(n)] for __ in range(n)] 
for i in range(n):
    cost[i][i]=0

ans = []
for _ in range(k):
    tmp = list(map(int, input().split()))
    if tmp[0]==0: # chumon
        a = tmp[1]-1
        b = tmp[2]-1 
        if cost[a][b]<float("inf"):
            ans.append(cost[a][b])
            #print(cost[a][b]) 
        else:
            ans.append(-1)
            #print(-1)
    else: # add
        c = tmp[1]-1 # port
        d = tmp[2]-1 # port
        e = tmp[3]   # cost
        for a in range(n):
            for b in range(n):
                cost[a][b] = min(cost[a][b], 
                                 cost[a][c] + e + cost[d][b],
                                 cost[a][d] + e + cost[c][b]) 
 
print(*ans, sep='\n')