(* 目的: 鶴の数に応じた足の本数を計算する *)
(* tsuru_no_ashi : int -> int *)
let tsuru_no_ashi x = x * 2

(* テスト *)
let test1 = tsuru_no_ashi 25 = 50
let test2 = tsuru_no_ashi 28 = 56
let test3 = tsuru_no_ashi 31 = 62



(* 目的: 亀の数に応じた足の本数を計算する *)
(* kame_no_ashi : int -> int *)
let kame_no_ashi x = x * 4

(* テスト *)
let test1 = kame_no_ashi 25 = 100
let test2 = kame_no_ashi 28 = 112
let test3 = kame_no_ashi 31 = 124




(* 目的: 鶴、亀の数に応じた足の本数を計算する *)
(* tsurukame_no_ashi : int -> int -> int *)
let tsurukame_no_ashi x y = x * 2 + y * 4

(* テスト *)
let test1 = tsurukame_no_ashi 0 2 = 8
let test2 = tsurukame_no_ashi 5 7 = 38
let test3 = tsurukame_no_ashi 11 0 = 22




(* 目的: 鶴と亀の合計の数と、足の数の合計から、鶴の数計算する *)
(* tsurukame : int -> int -> int *)
let tsurukame num ashi = - ashi / 2 + 2 * num


(* テスト *)

(* let test1 = tsurukame x+y (tsuru_no_ashi x + kame_no_ashi y) = x *)
let test1 = tsurukame (1+10) (tsuru_no_ashi 1 + kame_no_ashi 10) = 1
let test2 = tsurukame (7+5) (tsuru_no_ashi 7 + kame_no_ashi 5) = 7
let test2 = tsurukame (13+17) (tsuru_no_ashi 13 + kame_no_ashi 17) = 13







(*
num = x + y => y = num - x
ashi = x * 2 + y * 4

ashi = x * 2 + (num - x)*4
ashi = - 2 * x + 4 * num
x = - ashi / 2 + 2 * num
*)