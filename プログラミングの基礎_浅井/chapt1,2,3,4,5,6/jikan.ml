(* 目的: 時間を受け取ったら、午前か、午後を返す。 *)
(* jikan : int -> string *)
let jikan h = if h >= 0 && h < 12 then "午前"
                                  else "午後"


(* テスト *)
let test1 = jikan 0 = "午前"
let test2 = jikan 1 = "午前"
let test3 = jikan 11 = "午前"
let test4 = jikan 12 = "午後"
let test5 = jikan 13 = "午後"
let test6 = jikan 24 = "午後"