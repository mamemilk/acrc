# https://atcoder.jp/contests/abc178/tasks/abc178_d
# 
# 以下の感じで，動的計画法が使える．
# sumのメモ化がきっとできるのだが，40msec程度なので，よしとする．
# 
#   0
#   1
#   2
#   3: {3}
#   4: {4}
#   5: {5}
#   6: {6}，(3の結果から求まる） {3,3}
#   7: {7}, (3の結果から求まる） {3,4} (3の結果から求まる） {4,3}

S = int (input ())
M = 1000000007
ans= []
ans.append (0) #0
ans.append (0) #1
ans.append (0) #2
ans.append (1) #3
ans.append (1) #4
ans.append (1) #5

n= 5

while n < S:
    pre = 1 + sum(ans[:n-1])
    pre %= M
    ans.append(pre)
    n +=1

print(ans[S])
