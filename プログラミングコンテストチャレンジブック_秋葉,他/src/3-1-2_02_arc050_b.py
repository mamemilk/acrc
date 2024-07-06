# https://atcoder.jp/contests/arc050/tasks/arc050_b
# 
# 本当は不等式で線形計画法的に解きたかったが実力及ばず．二分探索する．
# 
# x 本の赤い花と 1 本の青い花からなる花束 : a set 
# 1 本の赤い花と y 本の青い花からなる花束 : b set
#  
# R >= ax + b 
# B >= by + a
# を満たす, a+bの最大値 (a>=0, b>=0)
#
# 公式解説で意味がわからず，https://speakerdeck.com/poyo/arc-050-b-hua-shu?slide=9 
# の絵を見てようやく理解．．．
# 

R, B = map(int, input().split())
x, y = map(int, input().split())

left, right = 0, max(R,B) # leftはOK，rightはNG

while left+1 != right:
    half = (left + right) // 2

    is_ok = (R-half)/(x-1) + (B-half)//(y-1) >= half

    if is_ok: 
        left, rigt = half, right 
    else : 
        left, right = left, half
        
print(left)
