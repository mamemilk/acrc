# https://atcoder.jp/contests/abc076/tasks/abc076_c
# 
# 

S = input()
T = input()

ans = []

def match(A,B):
    for a, b in zip(A,B):
        if a=='?':
            continue
        elif a!=b:
            return False
    return True


for i in range(len(S)-len(T)+1):
    if match(S[i:i+len(T)], T):
        tmp = S[:i] + T + S[i+len(T):]
        ans.append(tmp.replace('?', 'a'))

if len(ans) == 0:
    print('UNRESTORABLE')
else:
    print(min(ans))