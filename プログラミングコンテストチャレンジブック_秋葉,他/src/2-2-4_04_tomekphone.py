# https://community.topcoder.com/stat?c=problem_statement&pm=12296

frequencies = list(map(int, input().split(',')))
keySizes = list(map(int, input().split(',')))

charNum = len(frequencies)
keyNum = len(keySizes)


if charNum > sum(keySizes):
    print(-1)


frequencies.sort(reverse=True)


availableNumPerStroke = [0 for _ in range(max(keySizes))] # [0] = number of keys which allows 1 stroke.
for keySize in keySizes:
    for i in range(keySize):
        availableNumPerStroke[i] += 1


ans = 0
tempNumStroke = 1
for f in frequencies:
    if len(availableNumPerStroke) == 0:
        print(-1)
        exit(0)

    ans += tempNumStroke * f
    availableNumPerStroke[0] -= 1
    if availableNumPerStroke[0] == 0:
        availableNumPerStroke.pop(0)
        tempNumStroke += 1

print(ans)
        

