'''
https://atcoder.jp/contests/abc167/tasks/abc167_d

N : 2*(10**5)
K : 10**18

Nに対して，Kが大きいので，ループが発生する．
一回でもいったことのある町にいったらそこえループが発生．

- visitedを，通過した町のリストで作り，通過チェックしたが，TLE．
- 通過チェックのみ，各町にフラグをつけて判別したら，TLE解消．


'''

N, K= map(int, input().split())
Ai = list(map(int, input().split()))
visited = []
visited2 = [False for i in Ai]

machi=1
visited.append(machi)
visited2[machi-1] = True

loop_found = False

for i in range(K):
    array_index= machi - 1
    machi = Ai[array_index]

    #if machi in visited: //これだと ここのチェックで，log(n)かかる．
    if visited2[machi-1]:
        first = visited.index(machi)
        loop_len =(len(visited)-first)
        loop_found = True
        break
    else:
        visited.append(machi)
        visited2[machi-1] = True


if loop_found:
    remaning = K - i -1 
    print(visited[first + (remaning % loop_len)])
else:
    print(machi)
