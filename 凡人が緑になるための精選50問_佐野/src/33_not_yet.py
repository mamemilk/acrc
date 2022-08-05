# https://atcoder.jp/contests/abc177/tasks/abc177_d
# 
# 若干苦労した．
# 
# 友達グループA 1 2 3 4 
#            B 5 6 
#            C 7 8 9 
# この場合，同じグループに友達が居ないグループの分け方は，4グループ．
# 最大のグループの要素数が答えになる．
# 
# M == 0の場合を考慮せずにRuntime Errorになった．
# 1~Nまでで，出てこない人がいる場合の考慮をしておらずWrong Answerになった．
# 別のグループ同士が同じグループになるのを考慮せずにWrong Answerになった．
# ダメ元のパッチワークで修正したら，やっぱりTLEを連発．
# 

# N, M = map(int, input().split())

# group_id = -1
# names_by_id = {}
# id_by_name = {}

# vsame = {}

# for m in range(M):
#     a,b = map(int, input().split())

#     id_a = id_by_name.get(a, None)
#     id_b = id_by_name.get(b, None)
#     if id_a is None and id_b is None:
#         group_id += 1
#         id_by_name[a] = group_id
#         id_by_name[b] = group_id
#         names_by_id[group_id] = set([a,b])
#     elif id_a is not None and id_b is not None:
#         if id_a == id_b:
#             pass
#         else:
#             names_by_id[id_a] = names_by_id[id_a] | names_by_id[id_b]
#             names_by_id.pop(id_b)
            
#             if id_a in vsame.keys():
#                 vsame[id_a].add(id_b)
#             else:
#                 vsame[id_a] = set([id_b])
#             if id_b in vsame.keys():
#                 vsame[id_b].add(id_a)
#             else:
#                 vsame[id_b] = set([id_a])

#             # for k,v in id_by_name.items():
#             #     if v == id_b:
#             #         id_by_name[k] = id_a
#     elif id_a is not None:
#         id_by_name[b] = id_a
#         names_by_id[id_a].add(b)
#     else: # is_b:
#         id_by_name[a] = id_b
#         names_by_id[id_b].add(a)

# if M == 0:
#     print(1)
# else:
#     max_len = max([len(names) for names in names_by_id.values()])
#     min_len = min([len(names) for names in names_by_id.values()])
#     total   = sum([len(names) for names in names_by_id.values()])

#     if total != N:
#         print(max(max_len, min_len+1))
#     else:
#         print(max_len)

N, M = map(int, input().split())

friends_set_by_id = list(range(N))

for m in range(M):
    a,b = map(int, input().split())
    if type(friends_set_by_id[a-1]) is int and type(friends_set_by_id[b-1]) is int:
        friends_set_by_id[a-1] = set([a,b])
        friends_set_by_id[b-1] = friends_set_by_id[a-1]
    elif type(friends_set_by_id[b-1]) is int:
        friends_set_by_id[a-1].add(b)
        friends_set_by_id[b-1] = friends_set_by_id[a-1]
    elif type(friends_set_by_id[a-1]) is int:
        friends_set_by_id[b-1].add(a)
        friends_set_by_id[a-1] = friends_set_by_id[b-1]
    else:
        tmp = friends_set_by_id[a-1] | friends_set_by_id[b-1] 
        friends_set_by_id[a-1] = tmp
        friends_set_by_id[b-1] = tmp


#print(friends_set_by_id)

print(max([len(ele) if type(ele) is not int else 1 for ele in friends_set_by_id]))
