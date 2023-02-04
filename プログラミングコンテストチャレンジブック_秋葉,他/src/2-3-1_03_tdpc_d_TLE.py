N, D = map(int, input().split())

# これだとTLE 
# DP = [{'val': 1, 'prob': 1}]

# from functools import reduce 

# for _ in range(N):
#     リスト内包表記のこの書き方は初めて知りました．
#     pre = [{'val': ele['val']*val, 'prob': ele['prob']/6} for ele in DP for val in range(1,6+1)]

#     passed = []
#     waits  = []
#     for ele in pre:
#         if ele['val'] %D == 0:
#             passed.append(ele)
#         else:
#             waits.append(ele)
    
#     if len(passed) > 1:
#         # passed = [reduce(lambda a,b: {'val': D, 'prob': a['prob']+b['prob']}, filter(lambda ele: ele['val']%D==0, passed))]
#         passed = [reduce(lambda a,b: {'val': D, 'prob': a['prob']+b['prob']}, filter(lambda ele: ele['val']%D==0, passed))]
#     DP = waits + passed


print(DP[-1]['prob'])
