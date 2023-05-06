# https://atcoder.jp/contests/arc074/tasks/arc074_b
# 
# 
# 前半後半の区切りは，N~2Nのいずれか．
# この区切りを全探索することにする．

# import heapq

# N = int(input())
# A = list(map(int, input().split()))

# ans = []
# for k in range(N, 2*N+1):
#     zenhan = A[0:k]
#     kohan = A[k:]

#     heapq.heapify(zenhan)
#     while len(zenhan) > N:
#         heapq.heappop(zenhan)
    
#     kohan = list(map(lambda ele: -ele, kohan))
#     heapq.heapify(kohan)
#     while len(kohan) > N:
#         heapq.heappop(kohan)
    
#     ans.append(sum(zenhan) + sum(kohan))

# print(max(ans))


import heapq

N = int(input())
A = list(map(int, input().split()))

ans = []

zenhan = A[0:N]
heapq.heapify(zenhan)
Asum = sum(zenhan)
Asums = [Asum]
for a in A[N:2*N]:
    heapq.heappush(zenhan, a)
    aPop = heapq.heappop(zenhan)
    Asum += a - aPop
    Asums.append(Asum)

B = list(reversed(list(map(lambda ele: -ele, A))))
kohan = B[0:N]
heapq.heapify(kohan)
Bsum = sum(kohan)
Bsums = [Bsum]
for b in B[N:2*N]:
    heapq.heappush(kohan, b)
    bPop = heapq.heappop(kohan)
    Bsum += b - bPop
    Bsums.append(Bsum)

print(max(list(map(lambda ele: ele[0] + ele[1], zip(Asums, list(reversed(Bsums)))))))
