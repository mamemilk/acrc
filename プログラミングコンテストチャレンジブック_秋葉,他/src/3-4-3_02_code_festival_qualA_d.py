# https://atcoder.jp/contests/code-festival-2014-quala/tasks/code_festival_qualA_d

#　上の桁から、ある桁数まではAと同じ
#　その次の桁で異なる数字
#　以降の桁は、一番大きな数字もしくは一番小さな数字が連続する。
#　A<=10^15で、16桁
#　どの桁まで元の数と同じか？ p
#　

A, K = map(int, input().split())
Astr = str(A)
ans = float('inf')
for p in range(len(Astr)):
    for i in range(10):
        for j in range(10):
            Candidstr = Astr[:p] + str(i) + str(j) * (len(Astr)-p-1)
            Candid    = int(Candidstr)
            Candidstr = str(Candidstr)
            if len(set(Candidstr)) <= K:
                ans = min(abs(Candid - A), ans)
                print(Candidstr, ans)

print(ans)