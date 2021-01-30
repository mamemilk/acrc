
type ekimei_t = {
  kanji   : string;
  kana    : string;
  romaji  : string;
  shozoku : string;
}



let hyoji eki = match eki with
  {kanji=kanji; shozoku=shozoku; kana=kana;} -> shozoku ^ ", " ^ kanji ^ " (" ^ kana ^ ") "







(* test *)

let myogadani = {
  kanji = "茗荷谷";
  kana = "みょうがだに";
  romaji = "myogadani";
  shozoku="丸ノ内線";
};;

hyoji myogadani ;;