# N 点とるなら重なりの最大数
#　N-1点とるなら、重なりの最大数になってるものを抜いたときの最大数

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

timetoindex = {t: index for index, t in enumerate(sorted(set(sum(a, []))))}
indextotime = {index: t for index, t in enumerate(sorted(set(sum(a, []))))}

grid = [0 for _ in range(len(timetoindex))]

# print(timetoindex)

slong = 0 
tlong = 0
for s, t in a:
    s_index = timetoindex[s]
    t_index = timetoindex[t]
    grid[s_index] += 1
    grid[t_index] -= 1

    if t - s > tlong - slong:
        slong = s_index
        tlong = t_index


# print(slong, tlong)
grid[slong] -= 1
grid[tlong] += 1

for i in range(1, len(grid)):
    grid[i] += grid[i-1]

print(max(grid))
