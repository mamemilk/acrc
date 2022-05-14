# https://atcoder.jp/contests/abc182/tasks/abc182_c

import itertools

N = int(input())

def is_3dividable(N):
    s = sum([int(s) for s in str(N)])
    if s % 3 == 0:
        return True
    else:
        return False

k= len(str(N))
is_found = False
for e in range(k):
    for a in itertools.combinations(range(k), e):
        n = str(N)
        
        removed = ['-' if i in a else s for i,s in enumerate(n)]
        removed2 = list(filter(lambda a:a != '-', removed))
        if is_3dividable(int(''.join(removed2))):
            print(e)
            break

    if is_found:
        break

if not is_found:
    print(-1)