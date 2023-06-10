# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a

val = int(input())

badget = 1000 
coins = [500, 100, 50, 10, 5, 1]
tmp = badget - val 

ans = 0
index = 0

while tmp > 0:
    num = tmp // coins[index]
    ans += num
    tmp = tmp % coins[index]

    index += 1 

print(ans)

