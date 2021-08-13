# 勉強記録

こちらの本を勉強。

> [Linuxで動かしながら学ぶTCP/IPネットワーク入門](https://www.amazon.co.jp/Linuxで動かしながら学ぶTCP-IPネットワーク入門-もみじあめ-ebook/dp/B085BG8CH5)

network namespaceという技術で、linux上に仮想的なネットワークを構築しつつ、
パケットの流れをみる。

サポートページがあることを、最終章読んでるときに気付きました。

https://github.com/momijiame/linux-tcpip-book


## ハードウェア側の話も知りたく、Ethernet Controllerチップの仕様書も読んでみる。

https://docs.rs-online.com/8fdc/0900766b80dc9bce.pdf

### 1章　諸元、端子表、ブロック図
主要諸元
- IEEE 802.3
  (https://fujikura-solutions.co.jp/technology/104/) 80年2月に標準化会合スタートしたから802
- インテグレーティッドMACと、10Base-T PHY
  100, 1000は、別PHY?と思ったが、100, 1000はコンパチだが、速度は10Baseってことだと思われる。
- 10Base-Tでは、極性検出と極性変換対応
- 全二重、半二重
- データ故障時プログラマブル再送
- プログラマブルパディング、CRC生成
- プログラマブルリジェクション
- SPI 20MHz


バッファ諸元
- 8KByteの、送受信SRAM
  Dual Port -> リードとライトが同じタイミングでできる
- バッファサイズのコンフィグ可能
- ハード制御のリングFIFO
- バイト幅のインクリメントアクセス、ランダムアクセス？
- DMA内蔵
- Checksum

MAC諸元
- Unicast, Multicast, Broadcastパケット対応
- 何かの条件での"Wake-up"ホストが可能
  この場合のホストは、誰だ？


PHY諸元
- ループバック
- LEDアウトプット。（多分コネクタについてるやつ）

動作諸元
- 6割り込みソースで、1割り込み出力　（INT)
- 25MHz Clock入力
  SPI用には20MHz


### 2章 外部接続

- オシレータ接続図、
- Power-On Reset (REST端子)あとに、オシレータの安定待ち用に勝手に300usec待ってくれる。Power-On Resetから、300usecで安定するオシレータを使う、という意図と思われる。
- 300usecの間に、SPIアクセスしてもいいが、MACでの転送はしないでね、とのこと。
- カウンタ待ちの観測には、ESTAT.CLKRDYレジスタを使う。


CLKOUT pin
- システム上の他のディバイス用のクロックに使える、分周設定可能なクロック。MAC用の25MHzドメインで、どうやって使えるのかよくわからない。
  MACのあとにチップをさらに接続したりするとか？？



2.4章 : 外部の抵抗、コンデンサの接続指定。RJ45のみちょっと特殊。それ以外は、ノイズやプルダウン用。

2.5章 : 5Vでも動かせちゃうが、5Vで動かすとSPIも5Vになるから、レベルシフトして欲しい旨の説明。


### 3章　メモリ構成

- 制御レジスタ
- Ethernetバッファ
- PHYレジスタ

#### 制御レジスタ

- 4バンク構成（アドレスビット幅を抑えるため）


#### Ethernet バッファ

[受信の場合]

メモリポインタは、13bit=8Kbyte, レジスタ２wordで表現
- ERXSTH / ERXSTL = RX Start Byte (High, Low bytes)
- ERXNDH / ERXNDL = RX END Byte (High, Low bytes)


Ethernet IFからだのデータは、ST, NDの間をグルグルかかれる。

ホストがデータを引き取ったら、ポインタを更新する。引き取った領域までは、Ethernet IFがデータを書くが、
引き取られなかった場合は、データが破棄される。-> tcpの再送はホストが管理する？？


[送信の場合]

受信バッファで指定されてない部分は送信バッファ扱いになるっぽい。
送信時は、＼送信バッファに、ETXST / ETXNDを指定して、送信コマンドをホストが発行する。


#### PHYレジスタ



### SPIインターフェース

オペコード + Argumentのあとに、データを転送する。



### 5章 Ethernet

Ethernetのヘッダの説明。


### 6章 初期化

リセット方法の説明


### 7章　パケットの送受信

