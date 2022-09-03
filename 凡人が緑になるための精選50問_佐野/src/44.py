'''
https://atcoder.jp/contests/abc151/tasks/abc151_d

賢い方法が考えつかず，全探索．

'''

H, W = map(int, input().split())

maze = [["" for w in range(W)] for h in range(H)]

for h in range(H):
    wi = input()
    for w in range(W):
        maze[h][w] = wi[w]

# print(maze)

def check(start_h, start_w):
    if maze[start_h][start_w] == "#":
        return 0

    count = 0
    checkeds = [[-1 for i in range(W)] for i in range(H)]
    checkeds[start_h][start_w] = count

    nexts = [(start_h, start_w)]
    
    while len(nexts) > 0:
        count += 1 
        # print(nexts)
        _nexts = []
        for n in nexts:
            h, w = n
        
            # ue 
            if h - 1 >= 0 and checkeds[h-1][w]==-1 and maze[h-1][w] == '.':
                # print('ue', h-1, w, checkeds[h-1][w])
                checkeds[h-1][w] = count
                _nexts.append((h-1,w))

            # migi 
            if w + 1 < W and checkeds[h][w+1]==-1 and maze[h][w+1] == '.':
                # print('migi', h, w+1, checkeds[h][w+1])
                checkeds[h][w+1] = count
                _nexts.append((h,w+1))

            # sita 
            if h + 1 < H and checkeds[h+1][w]==-1 and maze[h+1][w] == '.':
                # print('sita', h+1, w, checkeds[h+1][w])
                checkeds[h+1][w] = count
                _nexts.append((h+1, w))

            # hidari
            if w - 1 >= 0 and checkeds[h][w-1]==-1 and maze[h][w-1] == '.':
                # print('hidari', h, w-1, checkeds[h][w-1])
                checkeds[h][w-1] = count
                _nexts.append((h, w-1))
        
        nexts = list(set(_nexts))
        # print()
    # print((start_h, start_w), checkeds, count)
    # print('    ')

    return count - 1
            

candid = []
for h in range(H):
    for w in range(W):
        candid.append(check(h,w))

print(max(candid))