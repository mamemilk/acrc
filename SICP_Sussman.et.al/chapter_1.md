# Chapter.1.1.1~1.1.6
## 名前付けと環境 / Naming and the Environment

```lisp
(define size 2)
```

値(オブジェクト)と名前を記憶(associate with)しているものを環境(environment)という。

## 複合手続き(compound procedure)

```lisp
(define (square x) (* x x))

(square (+ 2 5))
49
```

squareと名付けた、複合手続き(compound procedure)を定義することができる

## 手続き適用の置換モデル(substitution model)

```lisp
(define (f a)
  (sum-of-squares (+ a 1) (* a 2)))
```

と定義された複合手続きがあるとする。

```lisp

; 手続きfは、以下のような置換モデル(substitution model)で実行される
(f 5)

(sum-of-squares (+ a 1) (* a 2))

(sum-of-squares (+ 5 1) (* 5 2))

(+ (square 6) (square 10))

(+ (* 6 6) (* 10 10))

(+ 36 100)

136

```

## 正規順(Normal order)と、適用順(Applicative order)

* 正規順序評価 = 完全に展開してから簡約する。
* 適用順序評価 = 引数を評価しながら展開する。Appyしながら、なので、Applicativeだと思われる。

正規順序の場合は、以下で(+ 5 1), (* 5 2)は展開された分だけ評価される
```lisp
(sum-of-squares (+ 5 1) (* 5 2))

(+    (square (+ 5 1)) (square (* 5 2)) )

(+    (* (+ 5 1) (+ 5 1)) (* (* 5 2) (* 5 2)))
```

Exercise1.5で、正規順序、適用順序の違いが出題されている。
```lisp
(test 0 (p))

;; 正規順序
(test 0 (p))
(if (= 0 (p))
  0
  (p))
;; => 0

;;適用順序
(test 0 (p))
;; => 0, (p)の評価を始めて無限ループ
```



## 条件式とプレディケート(Conditional Expressions and Predicates)

predicate = 根拠に基づく
という単語。日本語だと述語になるが、この文脈で丁度良い日本語がないのでプレディケートとした。

```lisp 
(define (abs x) 
  (cond ((> x 0) x) 
             ((= x 0) 0)
             ((< x 0) (- x))))

; condに続く式のペア
(<p> <e>)
; をclauses(節)と呼び、最初の式<p>をpredicateと呼ぶ。
; <e>はexpression(結果式)となる。
(cond (<p1> <e1>)
           (<p2> <e2>)
           ...
           (<pn> <en>))
```

consにおけるelse文や、if文は以下のようになる。

```lisp
(define (abs x)
  (cond ((< x 0) (- x))
             (else x)))

(define (abs x) 
  (if (< x 0)
       (- x) x))
; このif文、エクセルのif文に似ている
(if (<predicate>) (<consequent> (<alternative>))
```


