# https://atcoder.jp/contests/abc149/tasks/abc149_d
# N個の手を，K個ずつ並べた1列が制約のかかる手になる．
# 1列ごとに制約を満たす最大の得点の手を決める．
# 同じ手の連続数だけを判別すればいいので，簡単．


N, K = map(int, input().split())
R, S, P = map(int, input().split())
T_pre=input()

Tate = []
for i in range(K):
    column = []
    for j in range(N//K+1):
        if j * K + i < N:
            column.append(T_pre[j * K + i])
    Tate.append(column)

points = {
    's' : R,
    'p' : S,
    'r' : P,
}

"""
    w : win
    l : lose

   [0] [1] [2] [3] 
   _______        
       _______       [1]がどんな手でも[1]!=[2]であれば[2]の最適解もしくは，[3]に影響しない手を選択できる
           _______


   同じ手が奇数回連続する場合，w l w l wの順番
"""

ans = 0
for one in Tate:
    #print(one)
    index = 0
    while index < len(one):
        ele = one[index]

        num = 1
        while index+num < len(one) and one[index+num]==ele:
            num += 1

        #print(num)
        if num == 0:
            ans += points[ele]
            #print(ele)
        elif num % 2==0:
            ans += num//2 * points[ele]
            #print(ele, '*')
        elif num % 2==1:
            ans += (num+1)//2 * points[ele]
            #print(ele, '*', ele)
        
        index = index+num

print(ans)

