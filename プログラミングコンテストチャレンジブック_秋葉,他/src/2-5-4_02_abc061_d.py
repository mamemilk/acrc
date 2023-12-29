# https://atcoder.jp/contests/abc061/tasks/abc061_d
# 
# 頂点 N に駒があるときのみ、ゲームを終了できます。
# 閉路の時，その閉路を一週して＋になったら無限に増やせる．
# 閉路の入り口で＋になっても，一週したときに収支マイナスになる場合があるのでそこを注意

# edge : [(s, t, d)], d: weight
def bellmanford_max(start,num_vertex,edges):
    d = [-float("inf")] * num_vertex
    d[start] = 0

    # 一週目．
    for _ in range(num_vertex-1):
        for p,q,r in edges:
            if d[p] != -float("inf") and d[q] < d[p] + r:
                d[q] = d[p] + r

    oneround = d[-1]

    # 閉路の判定，閉路があって閉路を通ったときの得点が＋になるなら
    for _ in range(num_vertex-1):
        for p,q,r in edges:
            if d[p] != -float("inf") and d[q] < d[p] + r:
                d[q] = d[p] + r

    tworound = d[-1]
    
    if oneround == tworound:
        return oneround
    else:
        return "inf"


N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a-1,b-1,c))

a = bellmanford_max(0, N, edges)
print(a)