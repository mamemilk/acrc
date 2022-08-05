# https://atcoder.jp/contests/abc204/tasks/abc204_c
# 最初setで実装し，TLEが4個．
# カンニングして，dequeで実装する．

from collections import deque

N, M = map(int, input().split())
AB = {}
for i in range(1,N+1):
    AB[i] = [i]

for i in range(M):
    A,B = map(int, input().split())
    AB[A].append(B)

#print(AB)

def count_ends_set(start):
    visited = set()
    visited.add(start)
    count = 1

    next_set = set(AB[start])
    while len(next_set - visited) > 0:
        for end in (next_set - visited):
            if end not in visited:
                count += 1
                visited.add(end)
                next_set = next_set | set(AB[end])
                next_set.discard(end)

    return count, next_set

def count_ends(start):
    visited = {k:False for k in AB.keys()}
    
    starts = deque([start])
    visited[start] = True
    count = 1
    
    while len(starts) > 0:
        a = starts.popleft()
        for b in AB[a]:
            if not visited[b]:
                count += 1
                starts.append(b)
                visited[b] = True
    return count, visited


res = 0
for start in AB.keys():
    count, next_set = count_ends(start)
    res += count
    #print(start, next_set)

print(res)

