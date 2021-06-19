
type ekimei_t = {
  kanji   : string; (* 駅名 *)
  kana    : string; (* 読み *)
  romaji  : string; (* ローマ字 *)
  shozoku : string; (* 所属線名 *)
}

type ekikan_t = {
  kiten  : string; (* 起点 *)
  shuten : string; (* 終点 *)
  keiyu  : string; (* 経由線名 *)
  kyori  : float;  (* 距離 *)
  jikan  : int;    (* 時間 *)
}

type eki_t = {
  namae        : string;  (* 漢字の駅名 *)
  saitan_kyori : float;   (* 最短距離 *)
  temae_list   : string list;    (* 漢字の駅名のリスト *)
}


let global_ekimei_list = [
{kanji="代々木上原"; kana="よよぎうえはら"; romaji="yoyogi-uehara"; shozoku="千代田線"};
{kanji="代々木公園"; kana="よよぎこうえん"; romaji="yoyogi-kouen"; shozoku="千代田線"};
{kanji="明治神宮前"; kana="めいじじんぐうまえ"; romaji="meiji-jinguumae"; shozoku="千代田線"};
{kanji="表参道"; kana="おもてさんどう"; romaji="omote-sando"; shozoku="千代田線"};
{kanji="乃木坂"; kana="のぎざか"; romaji="nogizaka"; shozoku="千代田線"};
{kanji="赤坂"; kana="あかさか"; romaji="akasaka"; shozoku="千代田線"};
{kanji="国会議事堂前"; kana="こっかいぎじどうまえ"; romaji="kokkai-gijidomae"; shozoku="千代田線"};
{kanji="霞ヶ関"; kana="かすみがせき"; romaji="kasumigaseki"; shozoku="千代田線"};
{kanji="日比谷"; kana="ひびや"; romaji="hibiya"; shozoku="千代田線"};
{kanji="二重橋前"; kana="にじゅうばしまえ"; romaji="nijuubasimae"; shozoku="千代田線"};
{kanji="大手町"; kana="おおてまち"; romaji="otemachi"; shozoku="千代田線"};
{kanji="新御茶ノ水"; kana="しんおちゃのみず"; romaji="shin-ochanomizu"; shozoku="千代田線"};
{kanji="湯島"; kana="ゆしま"; romaji="yushima"; shozoku="千代田線"};
{kanji="根津"; kana="ねづ"; romaji="nedu"; shozoku="千代田線"};
{kanji="千駄木"; kana="せんだぎ"; romaji="sendagi"; shozoku="千代田線"};
{kanji="西日暮里"; kana="にしにっぽり"; romaji="nishi-nippori"; shozoku="千代田線"};
{kanji="町屋"; kana="まちや"; romaji="machiya"; shozoku="千代田線"};
{kanji="北千住"; kana="きたせんじゅ"; romaji="kita-senju"; shozoku="千代田線"};
{kanji="綾瀬"; kana="あやせ"; romaji="ayase"; shozoku="千代田線"};
{kanji="北綾瀬"; kana="きたあやせ"; romaji="kita-ayase"; shozoku="千代田線"};
{kanji="浅草"; kana="あさくさ"; romaji="asakusa"; shozoku="銀座線"};
{kanji="田原町"; kana="たわらまち"; romaji="tawaramachi"; shozoku="銀座線"};
{kanji="稲荷町"; kana="いなりちょう"; romaji="inaricho"; shozoku="銀座線"};
{kanji="上野"; kana="うえの"; romaji="ueno"; shozoku="銀座線"};
{kanji="上野広小路"; kana="うえのひろこうじ"; romaji="ueno-hirokoji"; shozoku="銀座線"};
{kanji="末広町"; kana="すえひろちょう"; romaji="suehirocho"; shozoku="銀座線"};
{kanji="神田"; kana="かんだ"; romaji="kanda"; shozoku="銀座線"};
{kanji="三越前"; kana="みつこしまえ"; romaji="mitsukoshimae"; shozoku="銀座線"};
{kanji="日本橋"; kana="にほんばし"; romaji="nihonbashi"; shozoku="銀座線"};
{kanji="京橋"; kana="きょうばし"; romaji="kyobashi"; shozoku="銀座線"};
{kanji="銀座"; kana="ぎんざ"; romaji="ginza"; shozoku="銀座線"};
{kanji="新橋"; kana="しんばし"; romaji="shinbashi"; shozoku="銀座線"};
{kanji="虎ノ門"; kana="とらのもん"; romaji="toranomon"; shozoku="銀座線"};
{kanji="溜池山王"; kana="ためいけさんのう"; romaji="tameike-sanno"; shozoku="銀座線"};
{kanji="赤坂見附"; kana="あかさかみつけ"; romaji="akasaka-mitsuke"; shozoku="銀座線"};
{kanji="青山一丁目"; kana="あおやまいっちょうめ"; romaji="aoyama-itchome"; shozoku="銀座線"};
{kanji="外苑前"; kana="がいえんまえ"; romaji="gaienmae"; shozoku="銀座線"};
{kanji="表参道"; kana="おもてさんどう"; romaji="omote-sando"; shozoku="銀座線"};
{kanji="渋谷"; kana="しぶや"; romaji="shibuya"; shozoku="銀座線"};
{kanji="渋谷"; kana="しぶや"; romaji="shibuya"; shozoku="半蔵門線"};
{kanji="表参道"; kana="おもてさんどう"; romaji="omote-sando"; shozoku="半蔵門線"};
{kanji="青山一丁目"; kana="あおやまいっちょうめ"; romaji="aoyama-itchome"; shozoku="半蔵門線"};
{kanji="永田町"; kana="ながたちょう"; romaji="nagatacho"; shozoku="半蔵門線"};
{kanji="半蔵門"; kana="はんぞうもん"; romaji="hanzomon"; shozoku="半蔵門線"};
{kanji="九段下"; kana="くだんした"; romaji="kudanshita"; shozoku="半蔵門線"};
{kanji="神保町"; kana="じんぼうちょう"; romaji="jinbocho"; shozoku="半蔵門線"};
{kanji="大手町"; kana="おおてまち"; romaji="otemachi"; shozoku="半蔵門線"};
{kanji="三越前"; kana="みつこしまえ"; romaji="mitsukoshimae"; shozoku="半蔵門線"};
{kanji="水天宮前"; kana="すいてんぐうまえ"; romaji="suitengumae"; shozoku="半蔵門線"};
{kanji="清澄白河"; kana="きよすみしらかわ"; romaji="kiyosumi-shirakawa"; shozoku="半蔵門線"};
{kanji="住吉"; kana="すみよし"; romaji="sumiyoshi"; shozoku="半蔵門線"};
{kanji="錦糸町"; kana="きんしちょう"; romaji="kinshicho"; shozoku="半蔵門線"};
{kanji="押上"; kana="おしあげ"; romaji="oshiage"; shozoku="半蔵門線"};
{kanji="中目黒"; kana="なかめぐろ"; romaji="naka-meguro"; shozoku="日比谷線"};
{kanji="恵比寿"; kana="えびす"; romaji="ebisu"; shozoku="日比谷線"};
{kanji="広尾"; kana="ひろお"; romaji="hiro"; shozoku="日比谷線"};
{kanji="六本木"; kana="ろっぽんぎ"; romaji="roppongi"; shozoku="日比谷線"};
{kanji="神谷町"; kana="かみやちょう"; romaji="kamiyacho"; shozoku="日比谷線"};
{kanji="霞ヶ関"; kana="かすみがせき"; romaji="kasumigaseki"; shozoku="日比谷線"};
{kanji="日比谷"; kana="ひびや"; romaji="hibiya"; shozoku="日比谷線"};
{kanji="銀座"; kana="ぎんざ"; romaji="ginza"; shozoku="日比谷線"};
{kanji="東銀座"; kana="ひがしぎんざ"; romaji="higashi-ginza"; shozoku="日比谷線"};
{kanji="築地"; kana="つきじ"; romaji="tsukiji"; shozoku="日比谷線"};
{kanji="八丁堀"; kana="はっちょうぼり"; romaji="hacchobori"; shozoku="日比谷線"};
{kanji="茅場町"; kana="かやばちょう"; romaji="kayabacho"; shozoku="日比谷線"};
{kanji="人形町"; kana="にんぎょうちょう"; romaji="ningyomachi"; shozoku="日比谷線"};
{kanji="小伝馬町"; kana="こでんまちょう"; romaji="kodemmacho"; shozoku="日比谷線"};
{kanji="秋葉原"; kana="あきはばら"; romaji="akihabara"; shozoku="日比谷線"};
{kanji="仲御徒町"; kana="なかおかちまち"; romaji="naka-okachimachi"; shozoku="日比谷線"};
{kanji="上野"; kana="うえの"; romaji="ueno"; shozoku="日比谷線"};
{kanji="入谷"; kana="いりや"; romaji="iriya"; shozoku="日比谷線"};
{kanji="三ノ輪"; kana="みのわ"; romaji="minowa"; shozoku="日比谷線"};
{kanji="南千住"; kana="みなみせんじゅ"; romaji="minami-senju"; shozoku="日比谷線"};
{kanji="北千住"; kana="きたせんじゅ"; romaji="kita-senju"; shozoku="日比谷線"};
{kanji="池袋"; kana="いけぶくろ"; romaji="ikebukuro"; shozoku="丸ノ内線"};
{kanji="新大塚"; kana="しんおおつか"; romaji="shin-otsuka"; shozoku="丸ノ内線"};
{kanji="茗荷谷"; kana="みょうがだに"; romaji="myogadani"; shozoku="丸ノ内線"};
{kanji="後楽園"; kana="こうらくえん"; romaji="korakuen"; shozoku="丸ノ内線"};
{kanji="本郷三丁目"; kana="ほんごうさんちょうめ"; romaji="hongo-sanchome"; shozoku="丸ノ内線"};
{kanji="御茶ノ水"; kana="おちゃのみず"; romaji="ochanomizu"; shozoku="丸ノ内線"};
{kanji="淡路町"; kana="あわじちょう"; romaji="awajicho"; shozoku="丸ノ内線"};
{kanji="大手町"; kana="おおてまち"; romaji="otemachi"; shozoku="丸ノ内線"};
{kanji="東京"; kana="とうきょう"; romaji="tokyo"; shozoku="丸ノ内線"};
{kanji="銀座"; kana="ぎんざ"; romaji="ginza"; shozoku="丸ノ内線"};
{kanji="霞ヶ関"; kana="かすみがせき"; romaji="kasumigaseki"; shozoku="丸ノ内線"};
{kanji="国会議事堂前"; kana="こっかいぎじどうまえ"; romaji="kokkai-gijidomae"; shozoku="丸ノ内線"};
{kanji="赤坂見附"; kana="あかさかみつけ"; romaji="akasaka-mitsuke"; shozoku="丸ノ内線"};
{kanji="四ツ谷"; kana="よつや"; romaji="yotsuya"; shozoku="丸ノ内線"};
{kanji="四谷三丁目"; kana="よつやさんちょうめ"; romaji="yotsuya-sanchome"; shozoku="丸ノ内線"};
{kanji="新宿御苑前"; kana="しんじゅくぎょえんまえ"; romaji="shinjuku-gyoemmae"; shozoku="丸ノ内線"};
{kanji="新宿三丁目"; kana="しんじゅくさんちょうめ"; romaji="shinjuku-sanchome"; shozoku="丸ノ内線"};
{kanji="新宿"; kana="しんじゅく"; romaji="shinjuku"; shozoku="丸ノ内線"};
{kanji="西新宿"; kana="にししんじゅく"; romaji="nishi-shinjuku"; shozoku="丸ノ内線"};
{kanji="中野坂上"; kana="なかのさかうえ"; romaji="nakano-sakaue"; shozoku="丸ノ内線"};
{kanji="新中野"; kana="しんなかの"; romaji="shin-nakano"; shozoku="丸ノ内線"};
{kanji="東高円寺"; kana="ひがしこうえんじ"; romaji="higashi-koenji"; shozoku="丸ノ内線"};
{kanji="新高円寺"; kana="しんこうえんじ"; romaji="shin-koenji"; shozoku="丸ノ内線"};
{kanji="南阿佐ヶ谷"; kana="みなみあさがや"; romaji="minami-asagaya"; shozoku="丸ノ内線"};
{kanji="荻窪"; kana="おぎくぼ"; romaji="ogikubo"; shozoku="丸ノ内線"};
{kanji="中野新橋"; kana="なかのしんばし"; romaji="nakano-shimbashi"; shozoku="丸ノ内線"};
{kanji="中野富士見町"; kana="なかのふじみちょう"; romaji="nakano-fujimicho"; shozoku="丸ノ内線"};
{kanji="方南町"; kana="ほうなんちょう"; romaji="honancho"; shozoku="丸ノ内線"};
{kanji="四ツ谷"; kana="よつや"; romaji="yotsuya"; shozoku="南北線"};
{kanji="永田町"; kana="ながたちょう"; romaji="nagatacho"; shozoku="南北線"};
{kanji="溜池山王"; kana="ためいけさんのう"; romaji="tameike-sanno"; shozoku="南北線"};
{kanji="六本木一丁目"; kana="ろっぽんぎいっちょうめ"; romaji="roppongi-itchome"; shozoku="南北線"};
{kanji="麻布十番"; kana="あざぶじゅうばん"; romaji="azabu-juban"; shozoku="南北線"};
{kanji="白金高輪"; kana="しろかねたかなわ"; romaji="shirokane-takanawa"; shozoku="南北線"};
{kanji="白金台"; kana="しろかねだい"; romaji="shirokanedai"; shozoku="南北線"};
{kanji="目黒"; kana="めぐろ"; romaji="meguro"; shozoku="南北線"};
{kanji="市ヶ谷"; kana="いちがや"; romaji="ichigaya"; shozoku="南北線"};
{kanji="飯田橋"; kana="いいだばし"; romaji="iidabashi"; shozoku="南北線"};
{kanji="後楽園"; kana="こうらくえん"; romaji="korakuen"; shozoku="南北線"};
{kanji="東大前"; kana="とうだいまえ"; romaji="todaimae"; shozoku="南北線"};
{kanji="本駒込"; kana="ほんこまごめ"; romaji="hon-komagome"; shozoku="南北線"};
{kanji="駒込"; kana="こまごめ"; romaji="komagome"; shozoku="南北線"};
{kanji="西ヶ原"; kana="にしがはら"; romaji="nishigahara"; shozoku="南北線"};
{kanji="王子"; kana="おうじ"; romaji="oji"; shozoku="南北線"};
{kanji="王子神谷"; kana="おうじかみや"; romaji="oji-kamiya"; shozoku="南北線"};
{kanji="志茂"; kana="しも"; romaji="shimo"; shozoku="南北線"};
{kanji="赤羽岩淵"; kana="あかばねいわぶち"; romaji="akabane-iwabuchi"; shozoku="南北線"};
{kanji="西船橋"; kana="にしふなばし"; romaji="nishi-funabashi"; shozoku="東西線"};
{kanji="原木中山"; kana="ばらきなかやま"; romaji="baraki-nakayama"; shozoku="東西線"};
{kanji="妙典"; kana="みょうでん"; romaji="myoden"; shozoku="東西線"};
{kanji="行徳"; kana="ぎょうとく"; romaji="gyotoku"; shozoku="東西線"};
{kanji="南行徳"; kana="みなみぎょうとく"; romaji="minami-gyotoku"; shozoku="東西線"};
{kanji="浦安"; kana="うらやす"; romaji="urayasu"; shozoku="東西線"};
{kanji="葛西"; kana="かさい"; romaji="kasai"; shozoku="東西線"};
{kanji="西葛西"; kana="にしかさい"; romaji="nishi-kasai"; shozoku="東西線"};
{kanji="南砂町"; kana="みなみすなまち"; romaji="minami-sunamachi"; shozoku="東西線"};
{kanji="東陽町"; kana="とうようちょう"; romaji="touyoucho"; shozoku="東西線"};
{kanji="木場"; kana="きば"; romaji="kiba"; shozoku="東西線"};
{kanji="門前仲町"; kana="もんぜんなかちょう"; romaji="monzen-nakacho"; shozoku="東西線"};
{kanji="茅場町"; kana="かやばちょう"; romaji="kayabacho"; shozoku="東西線"};
{kanji="日本橋"; kana="にほんばし"; romaji="nihonbashi"; shozoku="東西線"};
{kanji="大手町"; kana="おおてまち"; romaji="otemachi"; shozoku="東西線"};
{kanji="竹橋"; kana="たけばし"; romaji="takebashi"; shozoku="東西線"};
{kanji="九段下"; kana="くだんした"; romaji="kudanshita"; shozoku="東西線"};
{kanji="飯田橋"; kana="いいだばし"; romaji="iidabashi"; shozoku="東西線"};
{kanji="神楽坂"; kana="かぐらざか"; romaji="kagurazaka"; shozoku="東西線"};
{kanji="早稲田"; kana="わせだ"; romaji="waseda"; shozoku="東西線"};
{kanji="高田馬場"; kana="たかだのばば"; romaji="takadanobaba"; shozoku="東西線"};
{kanji="落合"; kana="おちあい"; romaji="ochiai"; shozoku="東西線"};
{kanji="中野"; kana="なかの"; romaji="nakano"; shozoku="東西線"};
{kanji="新木場"; kana="しんきば"; romaji="shin-kiba"; shozoku="有楽町線"};
{kanji="辰巳"; kana="たつみ"; romaji="tatsumi"; shozoku="有楽町線"};
{kanji="豊洲"; kana="とよす"; romaji="toyosu"; shozoku="有楽町線"};
{kanji="月島"; kana="つきしま"; romaji="tsukishima"; shozoku="有楽町線"};
{kanji="新富町"; kana="しんとみちょう"; romaji="shintomicho"; shozoku="有楽町線"};
{kanji="銀座一丁目"; kana="ぎんざいっちょうめ"; romaji="ginza-itchome"; shozoku="有楽町線"};
{kanji="有楽町"; kana="ゆうらくちょう"; romaji="yurakucho"; shozoku="有楽町線"};
{kanji="桜田門"; kana="さくらだもん"; romaji="sakuradamon"; shozoku="有楽町線"};
{kanji="永田町"; kana="ながたちょう"; romaji="nagatacho"; shozoku="有楽町線"};
{kanji="麹町"; kana="こうじまち"; romaji="koujimachi"; shozoku="有楽町線"};
{kanji="市ヶ谷"; kana="いちがや"; romaji="ichigaya"; shozoku="有楽町線"};
{kanji="飯田橋"; kana="いいだばし"; romaji="iidabashi"; shozoku="有楽町線"};
{kanji="江戸川橋"; kana="えどがわばし"; romaji="edogawabasi"; shozoku="有楽町線"};
{kanji="護国寺"; kana="ごこくじ"; romaji="gokokuji"; shozoku="有楽町線"};
{kanji="東池袋"; kana="ひがしいけぶくろ"; romaji="higasi-ikebukuro"; shozoku="有楽町線"};
{kanji="池袋"; kana="いけぶくろ"; romaji="ikebukuro"; shozoku="有楽町線"};
{kanji="要町"; kana="かなめちょう"; romaji="kanamecho"; shozoku="有楽町線"};
{kanji="千川"; kana="せんかわ"; romaji="senkawa"; shozoku="有楽町線"};
{kanji="小竹向原"; kana="こたけむかいはら"; romaji="kotake-mukaihara"; shozoku="有楽町線"};
{kanji="氷川台"; kana="ひかわだい"; romaji="hikawadai"; shozoku="有楽町線"};
{kanji="平和台"; kana="へいわだい"; romaji="heiwadai"; shozoku="有楽町線"};
{kanji="営団赤塚"; kana="えいだんあかつか"; romaji="eidan-akatsuka"; shozoku="有楽町線"};
{kanji="営団成増"; kana="えいだんなります"; romaji="eidan-narimasu"; shozoku="有楽町線"};
{kanji="和光市"; kana="わこうし"; romaji="wakousi"; shozoku="有楽町線"};
]


let global_ekikan_list = [
{kiten="代々木上原"; shuten="代々木公園"; keiyu="千代田線"; kyori=1.0; jikan=2};
{kiten="代々木公園"; shuten="明治神宮前"; keiyu="千代田線"; kyori=1.2; jikan=2};
{kiten="明治神宮前"; shuten="表参道"; keiyu="千代田線"; kyori=0.9; jikan=2};
{kiten="表参道"; shuten="乃木坂"; keiyu="千代田線"; kyori=1.4; jikan=3};
{kiten="乃木坂"; shuten="赤坂"; keiyu="千代田線"; kyori=1.1; jikan=2};
{kiten="赤坂"; shuten="国会議事堂前"; keiyu="千代田線"; kyori=0.8; jikan=1};
{kiten="国会議事堂前"; shuten="霞ヶ関"; keiyu="千代田線"; kyori=0.7; jikan=1};
{kiten="霞ヶ関"; shuten="日比谷"; keiyu="千代田線"; kyori=1.2; jikan=2};
{kiten="日比谷"; shuten="二重橋前"; keiyu="千代田線"; kyori=0.7; jikan=1};
{kiten="二重橋前"; shuten="大手町"; keiyu="千代田線"; kyori=0.7; jikan=1};
{kiten="大手町"; shuten="新御茶ノ水"; keiyu="千代田線"; kyori=1.3; jikan=2};
{kiten="新御茶ノ水"; shuten="湯島"; keiyu="千代田線"; kyori=1.2; jikan=2};
{kiten="湯島"; shuten="根津"; keiyu="千代田線"; kyori=1.2; jikan=2};
{kiten="根津"; shuten="千駄木"; keiyu="千代田線"; kyori=1.0; jikan=2};
{kiten="千駄木"; shuten="西日暮里"; keiyu="千代田線"; kyori=0.9; jikan=1};
{kiten="西日暮里"; shuten="町屋"; keiyu="千代田線"; kyori=1.7; jikan=2};
{kiten="町屋"; shuten="北千住"; keiyu="千代田線"; kyori=2.6; jikan=3};
{kiten="北千住"; shuten="綾瀬"; keiyu="千代田線"; kyori=2.5; jikan=3};
{kiten="綾瀬"; shuten="北綾瀬"; keiyu="千代田線"; kyori=2.1; jikan=4};
{kiten="浅草"; shuten="田原町"; keiyu="銀座線"; kyori=0.8; jikan=2};
{kiten="田原町"; shuten="稲荷町"; keiyu="銀座線"; kyori=0.7; jikan=1};
{kiten="稲荷町"; shuten="上野"; keiyu="銀座線"; kyori=0.7; jikan=2};
{kiten="上野"; shuten="上野広小路"; keiyu="銀座線"; kyori=0.5; jikan=2};
{kiten="上野広小路"; shuten="末広町"; keiyu="銀座線"; kyori=0.6; jikan=1};
{kiten="末広町"; shuten="神田"; keiyu="銀座線"; kyori=1.1; jikan=2};
{kiten="神田"; shuten="三越前"; keiyu="銀座線"; kyori=0.7; jikan=1};
{kiten="三越前"; shuten="日本橋"; keiyu="銀座線"; kyori=0.6; jikan=2};
{kiten="日本橋"; shuten="京橋"; keiyu="銀座線"; kyori=0.7; jikan=2};
{kiten="京橋"; shuten="銀座"; keiyu="銀座線"; kyori=0.7; jikan=1};
{kiten="銀座"; shuten="新橋"; keiyu="銀座線"; kyori=0.9; jikan=2};
{kiten="新橋"; shuten="虎ノ門"; keiyu="銀座線"; kyori=0.8; jikan=2};
{kiten="虎ノ門"; shuten="溜池山王"; keiyu="銀座線"; kyori=0.6; jikan=2};
{kiten="溜池山王"; shuten="赤坂見附"; keiyu="銀座線"; kyori=0.9; jikan=2};
{kiten="赤坂見附"; shuten="青山一丁目"; keiyu="銀座線"; kyori=1.3; jikan=2};
{kiten="青山一丁目"; shuten="外苑前"; keiyu="銀座線"; kyori=0.7; jikan=2};
{kiten="外苑前"; shuten="表参道"; keiyu="銀座線"; kyori=0.7; jikan=1};
{kiten="表参道"; shuten="渋谷"; keiyu="銀座線"; kyori=1.3; jikan=1};
{kiten="渋谷"; shuten="表参道"; keiyu="半蔵門線"; kyori=1.3; jikan=2};
{kiten="表参道"; shuten="青山一丁目"; keiyu="半蔵門線"; kyori=1.4; jikan=2};
{kiten="青山一丁目"; shuten="永田町"; keiyu="半蔵門線"; kyori=1.3; jikan=2};
{kiten="永田町"; shuten="半蔵門"; keiyu="半蔵門線"; kyori=1.0; jikan=2};
{kiten="半蔵門"; shuten="九段下"; keiyu="半蔵門線"; kyori=1.6; jikan=2};
{kiten="九段下"; shuten="神保町"; keiyu="半蔵門線"; kyori=0.4; jikan=1};
{kiten="神保町"; shuten="大手町"; keiyu="半蔵門線"; kyori=1.7; jikan=3};
{kiten="大手町"; shuten="三越前"; keiyu="半蔵門線"; kyori=0.7; jikan=1};
{kiten="三越前"; shuten="水天宮前"; keiyu="半蔵門線"; kyori=1.3; jikan=2};
{kiten="水天宮前"; shuten="清澄白河"; keiyu="半蔵門線"; kyori=1.7; jikan=3};
{kiten="清澄白河"; shuten="住吉"; keiyu="半蔵門線"; kyori=1.9; jikan=3};
{kiten="住吉"; shuten="錦糸町"; keiyu="半蔵門線"; kyori=1.0; jikan=2};
{kiten="錦糸町"; shuten="押上"; keiyu="半蔵門線"; kyori=1.4; jikan=2};
{kiten="中目黒"; shuten="恵比寿"; keiyu="日比谷線"; kyori=1.0; jikan=2};
{kiten="恵比寿"; shuten="広尾"; keiyu="日比谷線"; kyori=1.5; jikan=3};
{kiten="広尾"; shuten="六本木"; keiyu="日比谷線"; kyori=1.7; jikan=3};
{kiten="六本木"; shuten="神谷町"; keiyu="日比谷線"; kyori=1.5; jikan=3};
{kiten="神谷町"; shuten="霞ヶ関"; keiyu="日比谷線"; kyori=1.3; jikan=2};
{kiten="霞ヶ関"; shuten="日比谷"; keiyu="日比谷線"; kyori=1.2; jikan=2};
{kiten="日比谷"; shuten="銀座"; keiyu="日比谷線"; kyori=0.4; jikan=1};
{kiten="銀座"; shuten="東銀座"; keiyu="日比谷線"; kyori=0.4; jikan=1};
{kiten="東銀座"; shuten="築地"; keiyu="日比谷線"; kyori=0.6; jikan=2};
{kiten="築地"; shuten="八丁堀"; keiyu="日比谷線"; kyori=1.0; jikan=2};
{kiten="八丁堀"; shuten="茅場町"; keiyu="日比谷線"; kyori=0.5; jikan=1};
{kiten="茅場町"; shuten="人形町"; keiyu="日比谷線"; kyori=0.9; jikan=2};
{kiten="人形町"; shuten="小伝馬町"; keiyu="日比谷線"; kyori=0.6; jikan=1};
{kiten="小伝馬町"; shuten="秋葉原"; keiyu="日比谷線"; kyori=0.9; jikan=2};
{kiten="秋葉原"; shuten="仲御徒町"; keiyu="日比谷線"; kyori=1.0; jikan=1};
{kiten="仲御徒町"; shuten="上野"; keiyu="日比谷線"; kyori=0.5; jikan=1};
{kiten="上野"; shuten="入谷"; keiyu="日比谷線"; kyori=1.2; jikan=2};
{kiten="入谷"; shuten="三ノ輪"; keiyu="日比谷線"; kyori=1.2; jikan=2};
{kiten="三ノ輪"; shuten="南千住"; keiyu="日比谷線"; kyori=0.8; jikan=2};
{kiten="南千住"; shuten="北千住"; keiyu="日比谷線"; kyori=1.8; jikan=3};
{kiten="池袋"; shuten="新大塚"; keiyu="丸ノ内線"; kyori=1.8; jikan=3};
{kiten="新大塚"; shuten="茗荷谷"; keiyu="丸ノ内線"; kyori=1.2; jikan=2};
{kiten="茗荷谷"; shuten="後楽園"; keiyu="丸ノ内線"; kyori=1.8; jikan=2};
{kiten="後楽園"; shuten="本郷三丁目"; keiyu="丸ノ内線"; kyori=0.8; jikan=1};
{kiten="本郷三丁目"; shuten="御茶ノ水"; keiyu="丸ノ内線"; kyori=0.8; jikan=1};
{kiten="御茶ノ水"; shuten="淡路町"; keiyu="丸ノ内線"; kyori=0.8; jikan=1};
{kiten="淡路町"; shuten="大手町"; keiyu="丸ノ内線"; kyori=0.9; jikan=2};
{kiten="大手町"; shuten="東京"; keiyu="丸ノ内線"; kyori=0.6; jikan=1};
{kiten="東京"; shuten="銀座"; keiyu="丸ノ内線"; kyori=1.1; jikan=2};
{kiten="銀座"; shuten="霞ヶ関"; keiyu="丸ノ内線"; kyori=1.0; jikan=2};
{kiten="霞ヶ関"; shuten="国会議事堂前"; keiyu="丸ノ内線"; kyori=0.7; jikan=1};
{kiten="国会議事堂前"; shuten="赤坂見附"; keiyu="丸ノ内線"; kyori=0.9; jikan=2};
{kiten="赤坂見附"; shuten="四ツ谷"; keiyu="丸ノ内線"; kyori=1.3; jikan=2};
{kiten="四ツ谷"; shuten="四谷三丁目"; keiyu="丸ノ内線"; kyori=1.0; jikan=2};
{kiten="四谷三丁目"; shuten="新宿御苑前"; keiyu="丸ノ内線"; kyori=0.9; jikan=1};
{kiten="新宿御苑前"; shuten="新宿三丁目"; keiyu="丸ノ内線"; kyori=0.7; jikan=1};
{kiten="新宿三丁目"; shuten="新宿"; keiyu="丸ノ内線"; kyori=0.3; jikan=1};
{kiten="新宿"; shuten="西新宿"; keiyu="丸ノ内線"; kyori=0.8; jikan=1};
{kiten="西新宿"; shuten="中野坂上"; keiyu="丸ノ内線"; kyori=1.1; jikan=2};
{kiten="中野坂上"; shuten="新中野"; keiyu="丸ノ内線"; kyori=1.1; jikan=2};
{kiten="新中野"; shuten="東高円寺"; keiyu="丸ノ内線"; kyori=1.0; jikan=1};
{kiten="東高円寺"; shuten="新高円寺"; keiyu="丸ノ内線"; kyori=0.9; jikan=1};
{kiten="新高円寺"; shuten="南阿佐ヶ谷"; keiyu="丸ノ内線"; kyori=1.2; jikan=2};
{kiten="南阿佐ヶ谷"; shuten="荻窪"; keiyu="丸ノ内線"; kyori=1.5; jikan=2};
{kiten="中野坂上"; shuten="中野新橋"; keiyu="丸ノ内線"; kyori=1.3; jikan=2};
{kiten="中野新橋"; shuten="中野富士見町"; keiyu="丸ノ内線"; kyori=0.6; jikan=1};
{kiten="中野富士見町"; shuten="方南町"; keiyu="丸ノ内線"; kyori=1.3; jikan=2};
{kiten="市ヶ谷"; shuten="四ツ谷"; keiyu="南北線"; kyori=1.0; jikan=2};
{kiten="四ツ谷"; shuten="永田町"; keiyu="南北線"; kyori=1.3; jikan=3};
{kiten="永田町"; shuten="溜池山王"; keiyu="南北線"; kyori=0.9; jikan=1};
{kiten="溜池山王"; shuten="六本木一丁目"; keiyu="南北線"; kyori=0.9; jikan=2};
{kiten="六本木一丁目"; shuten="麻布十番"; keiyu="南北線"; kyori=1.2; jikan=2};
{kiten="麻布十番"; shuten="白金高輪"; keiyu="南北線"; kyori=1.3; jikan=2};
{kiten="白金高輪"; shuten="白金台"; keiyu="南北線"; kyori=1.0; jikan=2};
{kiten="白金台"; shuten="目黒"; keiyu="南北線"; kyori=1.3; jikan=2};
{kiten="市ヶ谷"; shuten="飯田橋"; keiyu="南北線"; kyori=1.1; jikan=2};
{kiten="飯田橋"; shuten="後楽園"; keiyu="南北線"; kyori=1.4; jikan=2};
{kiten="後楽園"; shuten="東大前"; keiyu="南北線"; kyori=1.3; jikan=3};
{kiten="東大前"; shuten="本駒込"; keiyu="南北線"; kyori=0.9; jikan=2};
{kiten="本駒込"; shuten="駒込"; keiyu="南北線"; kyori=1.4; jikan=2};
{kiten="駒込"; shuten="西ヶ原"; keiyu="南北線"; kyori=1.4; jikan=2};
{kiten="西ヶ原"; shuten="王子"; keiyu="南北線"; kyori=1.0; jikan=2};
{kiten="王子"; shuten="王子神谷"; keiyu="南北線"; kyori=1.2; jikan=2};
{kiten="王子神谷"; shuten="志茂"; keiyu="南北線"; kyori=1.6; jikan=3};
{kiten="志茂"; shuten="赤羽岩淵"; keiyu="南北線"; kyori=1.1; jikan=2};
{kiten="西船橋"; shuten="原木中山"; keiyu="東西線"; kyori=1.9; jikan=3};
{kiten="原木中山"; shuten="妙典"; keiyu="東西線"; kyori=2.1; jikan=2};
{kiten="妙典"; shuten="行徳"; keiyu="東西線"; kyori=1.3; jikan=2};
{kiten="行徳"; shuten="南行徳"; keiyu="東西線"; kyori=1.5; jikan=2};
{kiten="南行徳"; shuten="浦安"; keiyu="東西線"; kyori=1.2; jikan=2};
{kiten="浦安"; shuten="葛西"; keiyu="東西線"; kyori=1.9; jikan=2};
{kiten="葛西"; shuten="西葛西"; keiyu="東西線"; kyori=1.2; jikan=2};
{kiten="西葛西"; shuten="南砂町"; keiyu="東西線"; kyori=2.7; jikan=2};
{kiten="南砂町"; shuten="東陽町"; keiyu="東西線"; kyori=1.2; jikan=2};
{kiten="東陽町"; shuten="木場"; keiyu="東西線"; kyori=0.9; jikan=1};
{kiten="木場"; shuten="門前仲町"; keiyu="東西線"; kyori=1.1; jikan=1};
{kiten="門前仲町"; shuten="茅場町"; keiyu="東西線"; kyori=1.8; jikan=2};
{kiten="茅場町"; shuten="日本橋"; keiyu="東西線"; kyori=0.5; jikan=1};
{kiten="日本橋"; shuten="大手町"; keiyu="東西線"; kyori=0.8; jikan=1};
{kiten="大手町"; shuten="竹橋"; keiyu="東西線"; kyori=1.0; jikan=2};
{kiten="竹橋"; shuten="九段下"; keiyu="東西線"; kyori=1.0; jikan=1};
{kiten="九段下"; shuten="飯田橋"; keiyu="東西線"; kyori=0.7; jikan=1};
{kiten="飯田橋"; shuten="神楽坂"; keiyu="東西線"; kyori=1.2; jikan=2};
{kiten="神楽坂"; shuten="早稲田"; keiyu="東西線"; kyori=1.2; jikan=2};
{kiten="早稲田"; shuten="高田馬場"; keiyu="東西線"; kyori=1.7; jikan=3};
{kiten="高田馬場"; shuten="落合"; keiyu="東西線"; kyori=1.9; jikan=3};
{kiten="落合"; shuten="中野"; keiyu="東西線"; kyori=2.0; jikan=3};
{kiten="新木場"; shuten="辰巳"; keiyu="有楽町線"; kyori=1.5; jikan=2};
{kiten="辰巳"; shuten="豊洲"; keiyu="有楽町線"; kyori=1.7; jikan=2};
{kiten="豊洲"; shuten="月島"; keiyu="有楽町線"; kyori=1.4; jikan=2};
{kiten="月島"; shuten="新富町"; keiyu="有楽町線"; kyori=1.3; jikan=2};
{kiten="新富町"; shuten="銀座一丁目"; keiyu="有楽町線"; kyori=0.7; jikan=1};
{kiten="銀座一丁目"; shuten="有楽町"; keiyu="有楽町線"; kyori=0.5; jikan=1};
{kiten="有楽町"; shuten="桜田門"; keiyu="有楽町線"; kyori=1.0; jikan=1};
{kiten="桜田門"; shuten="永田町"; keiyu="有楽町線"; kyori=0.9; jikan=2};
{kiten="永田町"; shuten="麹町"; keiyu="有楽町線"; kyori=0.9; jikan=1};
{kiten="麹町"; shuten="市ヶ谷"; keiyu="有楽町線"; kyori=0.9; jikan=1};
{kiten="市ヶ谷"; shuten="飯田橋"; keiyu="有楽町線"; kyori=1.1; jikan=2};
{kiten="飯田橋"; shuten="江戸川橋"; keiyu="有楽町線"; kyori=1.6; jikan=3};
{kiten="江戸川橋"; shuten="護国寺"; keiyu="有楽町線"; kyori=1.3; jikan=2};
{kiten="護国寺"; shuten="東池袋"; keiyu="有楽町線"; kyori=1.1; jikan=2};
{kiten="東池袋"; shuten="池袋"; keiyu="有楽町線"; kyori=2.0; jikan=2};
{kiten="池袋"; shuten="要町"; keiyu="有楽町線"; kyori=1.2; jikan=2};
{kiten="要町"; shuten="千川"; keiyu="有楽町線"; kyori=1.0; jikan=1};
{kiten="千川"; shuten="小竹向原"; keiyu="有楽町線"; kyori=1.0; jikan=2};
{kiten="小竹向原"; shuten="氷川台"; keiyu="有楽町線"; kyori=1.5; jikan=2};
{kiten="氷川台"; shuten="平和台"; keiyu="有楽町線"; kyori=1.4; jikan=2};
{kiten="平和台"; shuten="営団赤塚"; keiyu="有楽町線"; kyori=1.8; jikan=2};
{kiten="営団赤塚"; shuten="営団成増"; keiyu="有楽町線"; kyori=1.5; jikan=2};
{kiten="営団成増"; shuten="和光市"; keiyu="有楽町線"; kyori=2.1; jikan=3};
]


let hyoji eki = match eki with
  {kanji=kanji; shozoku=shozoku; kana=kana;} -> shozoku ^ ", " ^ kanji ^ " (" ^ kana ^ ") "

let rec romaji_to_kanji romaji lst = match lst with
    [] -> ""
  | first :: rest ->
      if first.romaji = romaji then first.kanji
      else romaji_to_kanji romaji rest

let rec get_ekikan_kyori kanji1 kanji2 lst = match lst with
    [] -> infinity
  | first :: rest ->
      if ( first.kiten = kanji1 && first.shuten = kanji2 ) ||
         ( first.kiten = kanji2 && first.shuten = kanji1 ) then first.kyori
      else get_ekikan_kyori kanji1 kanji2 rest

let kyori_wo_hyoji romaji1 romaji2 =
  let kanji1 = romaji_to_kanji romaji1 global_ekimei_list in
  let kanji2 = romaji_to_kanji romaji2 global_ekimei_list in
  if      kanji1 = "" && kanji2 = "" then romaji1 ^ "という駅は存在しません。" ^ romaji2 ^ "という駅は存在しません。"
  else if kanji1 = ""                then romaji1 ^ "という駅は存在しません。"
  else if                kanji2 = "" then romaji2 ^ "という駅は存在しません。"
  else let kyori =  get_ekikan_kyori kanji1 kanji2 global_ekikan_list in
     if   kyori = infinity then kanji1 ^ "駅と" ^ kanji2 ^ "駅は繋がっていません。"
     else         kanji1 ^ "駅から" ^ kanji2 ^ "駅までは" ^ string_of_float(kyori) ^ "kmです。"

let rec make_eki_list_r lst = match lst with
    [] -> []
  | first :: rest -> {namae=first.kanji; saitan_kyori=infinity; temae_list=[]} :: make_eki_list_r rest

let make_eki_list lst = List.map (fun first -> {namae=first.kanji; saitan_kyori=infinity; temae_list=[]}) lst

let rec shokika_r lst kiten = match lst with
    [] -> []
  | first :: rest ->
      if first.namae = kiten then {namae=first.namae; saitan_kyori=0.; temae_list=[kiten]} :: shokika_r rest kiten
                             else first :: shokika_r rest kiten

let shokika lst kiten = List.map (fun first -> if first.namae = kiten then {namae=first.namae; saitan_kyori=0.; temae_list=[kiten]} else first) lst


let make_initial_eki_list lst kiten = List.map (fun eki -> if eki.kanji = kiten then {namae=eki.kanji; saitan_kyori=0.; temae_list=[kiten]}
                                                                                else {namae=eki.kanji; saitan_kyori=infinity; temae_list=[]}) lst

let rec seiretsu_insert lst n = match lst with
    [] -> [n]
  | first :: rest
       -> if first.kana <  n.kana then first :: seiretsu_insert rest n
                                  else n :: first :: rest

let rec seiretsu_sort lst = match lst with
    [] -> []
  | first :: rest
      -> seiretsu_insert (seiretsu_sort rest) first

let rec seiretsu_pre lst kana =
  match lst with
      [] -> []
    | first :: rest -> if first.kana = kana then (seiretsu_pre rest first.kana)
                                             else first :: (seiretsu_pre rest first.kana)

let seiretsu lst = let sorted = seiretsu_sort lst in
                   seiretsu_pre sorted ""

let koushin1 p q = let ekikan_kyori = get_ekikan_kyori p.namae q.namae global_ekikan_list in
                   if ekikan_kyori = infinity
                     then q
                     else
                       if ekikan_kyori +. p.saitan_kyori >= q.saitan_kyori
                         then q
                         else {namae=q.namae; saitan_kyori=ekikan_kyori +. p.saitan_kyori; temae_list=q.namae::p.temae_list}

(* let koushin p v = let koushin1 p q = let ekikan_kyori = get_ekikan_kyori p.namae q.namae global_ekikan_list in
                   if ekikan_kyori = infinity
                     then q
                     else
                       if ekikan_kyori +. p.saitan_kyori >= q.saitan_kyori
                         then q
                         else {namae=q.namae; saitan_kyori=ekikan_kyori +. p.saitan_kyori; temae_list=q.namae::p.temae_list} in
                  List.map (koushin1 p) v *)


let koushin p v ekikan_list = let koushin1 p q = let ekikan_kyori = get_ekikan_kyori p.namae q.namae ekikan_list in
                   if ekikan_kyori = infinity
                     then q
                     else
                       if ekikan_kyori +. p.saitan_kyori >= q.saitan_kyori
                         then q
                         else {namae=q.namae; saitan_kyori=ekikan_kyori +. p.saitan_kyori; temae_list=q.namae::p.temae_list} in
                  List.map (koushin1 p) v

let rec saitan_wo_bunri lst = match lst with
    [] -> ( {namae = "";  saitan_kyori = infinity; temae_list = []}, [] )
  | first :: rest ->
      let rest_res = saitan_wo_bunri rest in
      match rest_res with (min_rest, rest_rest) ->
      if first.saitan_kyori < min_rest.saitan_kyori then (first,    List.filter (fun ele -> not (ele.namae = first.namae)) lst)
                                                    else (min_rest, List.filter (fun ele -> not (ele.namae = min_rest.namae)) lst)

let print_eki eki = match eki with
  {namae = n; saitan_kyori = s; temae_list = lst} -> match lst with
      [] -> assert false (* この場合は起こりえない *)
    | [a] -> print_string (a ^ " : " ^ string_of_float s ^ "km");
	     print_newline ()
    | a :: rest -> List.fold_right (fun b () -> print_string (b ^ ","))
				   rest ();
		   print_string (a ^ " : " ^ string_of_float s ^ "km");
		   print_newline ()

let rec dijkstra_main lst ekikan_lst = match lst with
    [] -> []
  | lst -> let (p, v) = saitan_wo_bunri lst in
    p :: dijkstra_main (koushin p v ekikan_lst) ekikan_lst


let dijkstra shiten shuten =
  let shiten_kanji = romaji_to_kanji shiten global_ekimei_list in
  let shuten_kanji = romaji_to_kanji shuten global_ekimei_list in
  let eki_list = make_initial_eki_list global_ekimei_list shiten_kanji in
  let saitan_list = dijkstra_main eki_list global_ekikan_list in
  let rec get_eki lst eki = match lst with
      [] -> {namae=""; saitan_kyori=infinity; temae_list = []};
    | first :: rest -> if first.namae = shuten_kanji
                       then first
                       else get_eki rest eki in
   get_eki saitan_list shuten_kanji

let main romaji_kiten romaji_shuten =
  let eki = dijkstra romaji_kiten romaji_shuten in
  print_eki eki

let _ = main Sys.argv.(1) Sys.argv.(2)

(* test *)
let myogadani = {
  kanji = "茗荷谷";
  kana = "みょうがだに";
  romaji = "myogadani";
  shozoku="丸ノ内線";
}

let test1 = hyoji myogadani = "丸ノ内線, 茗荷谷 (みょうがだに) "

let test_list2 = [
 {kanji = "永田町"; kana = "ながたちょう"; romaji = "nagatacho"; shozoku = "有楽町線"};
 {kanji = "永田町"; kana = "ながたちょう"; romaji = "nagatacho"; shozoku = "南北線"};
 {kanji = "永田町"; kana = "ながたちょう"; romaji = "nagatacho"; shozoku = "半蔵門線"};
 {kanji = "西葛西"; kana = "にしかさい"; romaji = "nishi-kasai"; shozoku = "東西線"};
 {kanji = "西ヶ原"; kana = "にしがはら"; romaji = "nishigahara"; shozoku = "南北線"};
]

let test2 = seiretsu test_list2 = [
  {kanji = "永田町"; kana = "ながたちょう"; romaji = "nagatacho"; shozoku = "有楽町線"};
  {kanji = "西葛西"; kana = "にしかさい"; romaji = "nishi-kasai"; shozoku = "東西線"};
  {kanji = "西ヶ原"; kana = "にしがはら"; romaji = "nishigahara"; shozoku = "南北線"};
  ];;


let test_list3 = [
  {kanji="赤坂見附"; kana="あかさかみつけ"; romaji="akasaka-mitsuke"; shozoku="丸ノ内線"};
  {kanji="四ツ谷"; kana="よつや"; romaji="yotsuya"; shozoku="丸ノ内線"};
  {kanji="四谷三丁目"; kana="よつやさんちょうめ"; romaji="yotsuya-sanchome"; shozoku="丸ノ内線"};
  {kanji="新宿御苑前"; kana="しんじゅくぎょえんまえ"; romaji="shinjuku-gyoemmae"; shozoku="丸ノ内線"};
  {kanji="新宿三丁目"; kana="しんじゅくさんちょうめ"; romaji="shinjuku-sanchome"; shozoku="丸ノ内線"};
  {kanji="新宿"; kana="しんじゅく"; romaji="shinjuku"; shozoku="丸ノ内線"};
  {kanji="西新宿"; kana="にししんじゅく"; romaji="nishi-shinjuku"; shozoku="丸ノ内線"};
  {kanji="中野坂上"; kana="なかのさかうえ"; romaji="nakano-sakaue"; shozoku="丸ノ内線"};
  {kanji="新中野"; kana="しんなかの"; romaji="shin-nakano"; shozoku="丸ノ内線"};
  {kanji="東高円寺"; kana="ひがしこうえんじ"; romaji="higashi-koenji"; shozoku="丸ノ内線"};
  {kanji="新高円寺"; kana="しんこうえんじ"; romaji="shin-koenji"; shozoku="丸ノ内線"};
  {kanji="南阿佐ヶ谷"; kana="みなみあさがや"; romaji="minami-asagaya"; shozoku="丸ノ内線"};
  {kanji="荻窪"; kana="おぎくぼ"; romaji="ogikubo"; shozoku="丸ノ内線"};
  {kanji="中野新橋"; kana="なかのしんばし"; romaji="nakano-shimbashi"; shozoku="丸ノ内線"};
  {kanji="中野富士見町"; kana="なかのふじみちょう"; romaji="nakano-fujimicho"; shozoku="丸ノ内線"};
  {kanji="方南町"; kana="ほうなんちょう"; romaji="honancho"; shozoku="丸ノ内線"};
  {kanji="四ツ谷"; kana="よつや"; romaji="yotsuya"; shozoku="南北線"};
  ]

let test3 = seiretsu test_list3 = [
  {kanji = "赤坂見附"; kana = "あかさかみつけ"; romaji = "akasaka-mitsuke"; shozoku = "丸ノ内線"};
  {kanji = "荻窪"; kana = "おぎくぼ"; romaji = "ogikubo"; shozoku = "丸ノ内線"};
  {kanji = "新高円寺"; kana = "しんこうえんじ"; romaji = "shin-koenji"; shozoku = "丸ノ内線"};
  {kanji = "新宿"; kana = "しんじゅく"; romaji = "shinjuku"; shozoku = "丸ノ内線"};
  {kanji = "新宿御苑前"; kana = "しんじゅくぎょえんまえ"; romaji = "shinjuku-gyoemmae"; shozoku = "丸ノ内線"};
  {kanji = "新宿三丁目"; kana = "しんじゅくさんちょうめ"; romaji = "shinjuku-sanchome"; shozoku = "丸ノ内線"};
  {kanji = "新中野"; kana = "しんなかの"; romaji = "shin-nakano"; shozoku = "丸ノ内線"};
  {kanji = "中野坂上"; kana = "なかのさかうえ"; romaji = "nakano-sakaue"; shozoku = "丸ノ内線"};
  {kanji = "中野新橋"; kana = "なかのしんばし"; romaji = "nakano-shimbashi"; shozoku = "丸ノ内線"};
  {kanji = "中野富士見町"; kana = "なかのふじみちょう"; romaji = "nakano-fujimicho"; shozoku = "丸ノ内線"};
  {kanji = "西新宿"; kana = "にししんじゅく"; romaji = "nishi-shinjuku"; shozoku = "丸ノ内線"};
  {kanji = "東高円寺"; kana = "ひがしこうえんじ"; romaji = "higashi-koenji"; shozoku = "丸ノ内線"};
  {kanji = "方南町"; kana = "ほうなんちょう"; romaji = "honancho"; shozoku = "丸ノ内線"};
  {kanji = "南阿佐ヶ谷"; kana = "みなみあさがや"; romaji = "minami-asagaya"; shozoku = "丸ノ内線"};
  {kanji = "四ツ谷"; kana = "よつや"; romaji = "yotsuya"; shozoku = "丸ノ内線"};
  {kanji = "四谷三丁目"; kana = "よつやさんちょうめ"; romaji = "yotsuya-sanchome"; shozoku = "丸ノ内線"}]


let eki1 = {namae = "赤坂見附"   ;saitan_kyori = 1.3     ; temae_list = ["赤坂見附";"四ツ谷"]}
let eki2 = {namae = "国会議事堂前";saitan_kyori = infinity; temae_list = []}
let eki3 = {namae = "溜池山王"   ;saitan_kyori = infinity; temae_list = []}

let v = [eki2; eki3]

let test_koushin1 = koushin1 eki1 eki2 = {
  namae = "国会議事堂前"; saitan_kyori = 2.2; temae_list = ["国会議事堂前"; "赤坂見附"; "四ツ谷"]
  };;
let test_koushin = koushin eki1 v global_ekikan_list = [
  {namae = "国会議事堂前"; saitan_kyori = 2.2; temae_list = ["国会議事堂前"; "赤坂見附"; "四ツ谷"]};
  {namae = "溜池山王";    saitan_kyori = 2.2; temae_list = ["溜池山王"; "赤坂見附"; "四ツ谷"]}
  ];;




let seiretsu_global_ekimei_list = seiretsu global_ekimei_list
let eki_list = make_eki_list seiretsu_global_ekimei_list
let shokika_list_1 = shokika eki_list "青山一丁目"
let test_make_initial_eki_list = make_initial_eki_list seiretsu_global_ekimei_list "青山一丁目" = shokika_list_1;;


let test1 = dijkstra "tokyo" "ginza"
            = {namae = "銀座"; saitan_kyori = 1.1;
               temae_list = ["銀座"; "東京"]}
let test2 = dijkstra "tokyo" "shinjuku"
            = {namae = "新宿"; saitan_kyori = 7.9;
               temae_list = ["新宿"; "新宿三丁目"; "新宿御苑前";
                             "四谷三丁目"; "四ツ谷"; "赤坂見附";
                             "国会議事堂前"; "霞ヶ関"; "銀座"; "東京"]}


let rec assoc ekimei0 lst = match lst with
    [] -> infinity
  | (ekimei, kyori) :: rest ->
      if ekimei = ekimei0 then kyori else assoc ekimei0 rest

let test1 = assoc "後楽園" [] = infinity
let test2 = assoc "後楽園" [("新大塚", 1.2); ("後楽園", 1.8)] = 1.8
let test3 = assoc "池袋" [("新大塚", 1.2); ("後楽園", 1.8)] = infinity

type ekikan_tree_t =
    Empty
  | Node of ekikan_tree_t * string * (string * float) list * ekikan_tree_t


(* 片方向のデータを挿入する関数 *)
let rec insert1 ekikan_tree kiten shuten kyori = match ekikan_tree with
    Empty -> Node (Empty, kiten, [(shuten, kyori)], Empty)
  | Node (left, ekimei, lst, right) ->
      if kiten < ekimei      then Node (insert1 left kiten shuten kyori, ekimei, lst,                    right)
      else if ekimei < kiten then Node (left,                            ekimei, lst,                    insert1 right kiten shuten kyori)
      else                        Node (left,                            ekimei, (shuten, kyori) :: lst, right)

(* ekikan_treeに、ekikanを両方向で挿入する。 *)
let insert_ekikan ekikan_tree ekikan = match ekikan with
  {kiten = kiten; shuten = shuten; keiyu = keiyu; kyori = kyori; jikan = jikan} ->
    insert1 (insert1 ekikan_tree shuten kiten kyori) kiten shuten kyori

let ekikan1 =
  {kiten="池袋"; shuten="新大塚"; keiyu="丸ノ内線"; kyori=1.8; jikan=3}
let ekikan2 =
  {kiten="新大塚"; shuten="茗荷谷"; keiyu="丸ノ内線"; kyori=1.2; jikan=2}
let ekikan3 =
  {kiten="茗荷谷"; shuten="後楽園"; keiyu="丸ノ内線"; kyori=1.8; jikan=2}

let tree1 = insert_ekikan Empty ekikan1
let test1 = tree1 =
  Node (Empty, "新大塚", [("池袋", 1.8)],
	Node (Empty, "池袋", [("新大塚", 1.8)], Empty))
let tree2 = insert_ekikan tree1 ekikan2
let test2 = tree2 =
  Node (Empty, "新大塚", [("茗荷谷", 1.2); ("池袋", 1.8)],
	Node (Empty, "池袋", [("新大塚", 1.8)],
	      Node (Empty, "茗荷谷", [("新大塚", 1.2)], Empty)))
let tree3 = insert_ekikan tree2 ekikan3
let test3 = tree3 =
  Node (Node (Empty, "後楽園", [("茗荷谷", 1.8)], Empty),
	"新大塚", [("茗荷谷", 1.2); ("池袋", 1.8)],
        Node (Empty,
	      "池袋", [("新大塚", 1.8)],
	      Node (Empty,
		    "茗荷谷", [("後楽園", 1.8); ("新大塚", 1.2)],
		    Empty)));;

let inserts_ekikan ekikan_tree ekikan_list =
  List.fold_right (fun ekikan tree -> insert_ekikan tree ekikan)
		ekikan_list ekikan_tree;;


inserts_ekikan Empty [ekikan1; ekikan2; ekikan3];;


let test1 = inserts_ekikan Empty [ekikan1; ekikan2; ekikan3] =
  Node (Empty, "後楽園", [("茗荷谷", 1.8)],
    Node(
      Node (Empty, "新大塚", [("池袋", 1.8); ("茗荷谷", 1.2)],Node (Empty, "池袋", [("新大塚", 1.8)], Empty)),
      "茗荷谷",
      [("新大塚", 1.2); ("後楽園", 1.8)], Empty
    )
  );;

let rec get_ekikan_kyori kanji1 kanji2 tree = match tree with
    Empty -> infinity
  | Node (left, k, lst, right) ->
      if      kanji1 < k then get_ekikan_kyori kanji1 kanji2 left
      else if kanji1 > k then get_ekikan_kyori kanji1 kanji2 right
      else assoc kanji2 lst


let global_ekikan_tree = inserts_ekikan Empty global_ekikan_list
let test1 = get_ekikan_kyori "茗荷谷" "新大塚" global_ekikan_tree = 1.2
let test2 = get_ekikan_kyori "茗荷谷" "池袋" global_ekikan_tree = infinity
let test3 = get_ekikan_kyori "東京" "大手町" global_ekikan_tree = 0.6





(* inserts_ekikan Empty global_ekikan_list;; *)



(* shokika_list_1;;
saitan_wo_bunri shokika_list_1;; *)

