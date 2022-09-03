# 

At Coderに触れるとっかかりとして，非常にありがたい本だった．
一部の回答は，よりよいものがあるのでは?と思ったが，プログラミングコンテストの特性上，
限られた時間で解けて2000msec以内で動く堅い方法を紹介されている，とも思った．

勉強会ででてきた別解で，興味深いものを以下に挙げる．

## No.21

総当たりの必要がなく，鳥海さんの以下コードがエレガント．
最小の個数は，W//Bに

```python
A, B, W = map(int, input().split())

W *= 1000
if W // A == W // B:
    if W % B == 0:
        print(W // A, W // A)
    else:
        print('UNSATISFIABLE')
else:
    if W % B == 0: 
        print(W // B, W // A)
    else:
        print(W // B + 1, W // A)

        W//B * (A~B) + (A~B) == W
```

## No.23

テキストは，pypyで高速化する紹介がされてたが，二分探索を使うことで，pythonでも時間内に解くことはできた．
[No.23 回答](./src/23.py)

## No.30

鳥海さんの回答がエレガント．

- A^5 - B^5 = (A - B)(A^4 + A^3*B + A^2*B^2 + A*B^3 + B^4)から，A-BはXの約数となる．
- Aは，d/2が最小値(これ以上だと，A^5-B^5が負になる)なので，そこから探索


```python
#!/usr/bin/env python3

X = int(input())

# A^5 - B^5 = (A - B)(A^4 + A^3*B + A^2*B^2 + A*B^3 + B^4)
# なので A - B は X の約数である
# X の約数を求める
div = []
n = 1
while n*n <= X:  
    if X % n == 0:
        div.append(n)
        d = X // n
        if n != d:
            div.append(d)
    n += 1
div.sort(reverse=True)

for d in div:
    A = (d + 1) // 2
    B = A - d
    while (ans := pow(A, 5) - pow(B, 5)) < X:
        A += 1
        B += 1
    if ans == X:
        print(A, B)
        exit()

```

## No.33 

Union Findを使わずとも，メモ化により高速化が可能．


## No.35

二分探索ではなく，桁数ごとに探索する．