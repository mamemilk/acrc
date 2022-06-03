# https://atcoder.jp/contests/abc189/tasks/abc189_c
# ヒストグラムを並べて，最大の長方形を探すイメージ．
# 最初に高さh=min(A)で，全領域を見る．min(A)を除いた左右で同じことをする．
# 最初，再帰で書いた．log2(10**5)で問題ないと考えたがこれは誤りで，最下層で10**5回呼ばれるので実行時エラーになる．
# python3 23_gen.py  | python3 23.py
# で，テストした．

N = int(input())
Ai = list(map(int, input().split()))

res = 0

target_list = [Ai]
while(len(target_list) != 0):
    target = target_list.pop(0)

    width = len(target)
    min_h = min(target)
    min_h_index = target.index(min_h)
    if res <= min_h * width:
        res = min_h * width
    
    left = target[:min_h_index]
    if len(left) != 0:
        target_list.append(left)

    if width > (min_h_index+1):
        right = target[min_h_index+1:]
        if len(right) != 0:
            target_list.append(right)
  

# def f(target):
#     global res
#     width = len(target)
#     if width == 0:
#         return

#     min_h = min(target)
#     min_h_index = target.index(min_h)
#     if res <= min_h * width:
#         res = min_h * width

#     left = target[:min_h_index]
#     f(left)

#     if width > (min_h_index+1):
#         right = target[min_h_index+1:]
#         f(right)

# f(Ai)
print(res)


    

