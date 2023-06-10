# https://atcoder.jp/contests/abc007/tasks/abc007_2
# 

A = input()

if len(A) > 1:
    print(A[:-1])
else:
    if A == 'a':
        print(-1)
    else :
        print('a')
