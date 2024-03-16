# Build Guide

## 部品

### 必須

| 名前 | 数 | 備考 |
|:-|:-|:-|
| PCB | 2枚 | |
| プレート | 2セット | |
| ProMicro | 2枚 | |
| TRRSジャック | 2個 | |
| TRS(3極)ケーブル | 1本 | TRRS(4極)ケーブルでも可 |
| タクトスイッチ | 2個 | |
| ダイオード | 42本 | ロープロの場合は表面実装のみ可 |
| キースイッチ | 42個 | |
| キーキャップ | 42個 | 1u 40個、1.5u 2個 |
| スペーサー M2 7.5mm | 10本 | ロープロの場合は 4.5mm |
| スペーサー M2 9mm or 11mm | 4本 | |
| ネジ M2 | 28本 | |
| クッションゴム | 10個 | |

### オプション

| 名前 | 数 | 備考 |
|:-|:-|:-|
| OLEDモジュール | 1 ~ 2枚 | |
| ピンヘッダ 4連 | 2つ | OLEDモジュールを使用する場合 |
| ピンソケット4連 | 2つ | OLEDモジュールを使用する場合 |
| SK6812MINI | 54個 | 上向き実装 42個、下向き実装 12個 |
| シリアルLEDテープ | 2本 | SK6812MINI との併用は想定していません |

![image](https://user-images.githubusercontent.com/736191/40734610-e1ca0136-6473-11e8-8ac7-7bfa4b843f93.png)

## 事前準備

ファームウェアを自分でビルドする場合は環境を整備するのに時間がかかるのではじめに取り掛かっておくことをおすすめします。\
詳しくは <https://github.com/foostan/crkbd/blob/master/doc/firmware_jp.md> を参照してください。

## 実装

PCBはリバーシブルになっているので、最初にどちらを左用/右用にするか決めます。

### ダイオード

#### ロープロファイルのキースイッチを使わない場合

写真の位置にダイオードを実装します。
どちらの面に実装するかは好みですが、Undergrow LEDを実装する場合は、干渉をさけるため表面に実装することをおすすめします。
なお、ロープロファイルのキースイッチを使う場合と同様に表面実装タイプを利用しても問題ありません。

![image](https://user-images.githubusercontent.com/736191/40736513-306a0976-6479-11e8-8f98-a88073919a71.png)

ダイオードには向きがあるので注意してください。

<- 実装前 | 実装後 ->

![image](https://user-images.githubusercontent.com/736191/40735282-bac94180-6475-11e8-96f9-1d1cc43b1ee9.png)

#### ロープロファイルのキースイッチを使う場合

ロープロファイルスイッチを利用する場合は、表面実装タイプのダイオードを利用し、必ず __裏面に実装してください__ 。表面に実装してしまうとトッププレートがダイオードと干渉してしまいます。

### LED(オプション)

キースイッチ裏のLED(7 ~ 27)は表面側が光るように実装し、その他(1 ~ 6)は裏面側が光るようにします。
下記がLEDを実装する位置です。

![image](https://user-images.githubusercontent.com/736191/40731604-62cee61e-646c-11e8-865f-829a48fa6be0.png)

下記のように __裏面から各LEDを実装します__ 。○印を基準としLEDの向きに注意して実装してください。

![image](https://user-images.githubusercontent.com/736191/40731605-62f840a4-646c-11e8-99d5-b3bdff709e9d.png)

1 ~ 6のLEDは側面のわずかに出ているパターン(写真上のピンク色)とPCBのパターン(写真上の青色)をはんだ付けします。
フラックスを塗った上で少量のはんだを半田ごてで取ってパターンの境目に押し付けるとうまくいきます。

![image](https://user-images.githubusercontent.com/736191/40733058-c0558402-646f-11e8-9718-e579fab4aaf5.png)

LEDの点灯チェックを行う場合は、上記写真の番号どおりにつながっているため、途中までしか点灯しない場合は点灯しないLEDか、その一つ手前のLEDの実装ミスの可能性が高いので確認してみてください。

### OLEDモジュールのためのジャンパ(オプション)

OLEDモジュールを利用する場合は下記のようにジャンパします。
なお __表面のみジャンパしてください__ 。

![image](https://user-images.githubusercontent.com/736191/40734778-56ded514-6474-11e8-8da7-3ebba048d62d.png)

### TRRSジャック、リセットスイッチ、OLEDピンソケット(オプション)

下記の写真通りにTRRSジャック、リセットスイッチを実装します。
またOLEDモジュールを使用する場合は、ピンソケットを実装します。

![image](https://user-images.githubusercontent.com/736191/40736856-1bda2b84-647a-11e8-988b-dc45f2c76a38.png)

### ProMicro

ピンヘッダを白い枠に当てはめるように実装し、そこにProMicroの裏面を上にして実装します。
なお下記の写真は右手用ですが、左手用も同様に白枠にピンヘッダを実装し、ProMicroの裏面を上にして実装します。

![image](https://user-images.githubusercontent.com/736191/40737973-3f404de4-647d-11e8-84fe-37f3a34e4c53.png)

### OLEDモジュール

OLEDモジュールにピンヘッダを実装し、ピンソケットに差し込みます。

![image](https://user-images.githubusercontent.com/736191/40888530-7420d1aa-6793-11e8-8813-9681c1411a21.png)

ピンソケットとピンヘッダの高さによって利用するスペーサーの高さを調節してください。
写真では電子部品店で入手可能な一般的なピンソケットとピンヘッダと11mmのスペーサーを利用した例となります。

### ProMicroのソケット化

ProMicroをソケット化をすることでProMicroが故障してしまった場合に容易に取り替えが可能になります。
2パターンのソケット化を紹介します。

#### スプリングヘッダを利用したソケット化

ソケット化を可能とする特殊なピンヘッダを利用する方法です。
利用方法はHelixのビルドガイドを参考にしてください。
<https://github.com/MakotoKurauchi/helix/blob/master/Doc/buildguide_jp.md#pro-micro>

スプリングヘッダとProMicroのセットは遊舎工房にて購入することが可能です。

<https://yushakobo.jp/shop/promicro-spring-pinheader/>

同じく遊舎工房で購入可能なOLEDについてくるピンヘッダを利用すると以下のように隙間なくきれいに収まります。また9mmのスペーサーを利用することができるのでより薄い仕上がりとなります。

![img_4141](https://user-images.githubusercontent.com/736191/41304818-2b65511e-6eac-11e8-9357-999ff14080ed.png)

#### ピンソケットを利用したソケット化

秋月電子等で購入可能な背の低いピンソケットを利用した方法です。
多少の工作が必要となります。

<http://akizukidenshi.com/catalog/g/gC-03138/>

12個連結ピンソケット2つ用意し、ブレッドボード等に固定します。

![img_4130](https://user-images.githubusercontent.com/736191/41305246-4d63b7a0-6ead-11e8-8dbe-16c75d8b55e3.png)

ProMicroに付属しているピンヘッダProMicroを挟むようにして上からしっかりと差し込みます。

![img_4131](https://user-images.githubusercontent.com/736191/41305247-4fbd3e5e-6ead-11e8-8c4d-5feea5a026d3.png)

ピンヘッダとProMicroをはんだ付けした後に余分なピンヘッダを切り取れば完了です。

![img_4132](https://user-images.githubusercontent.com/736191/41305251-5198439a-6ead-11e8-80f4-bd1769915bc9.png)

#### 比較

下記はスプリングヘッダを利用した場合とピンソケットを利用した場合の比較になります。
スプリングヘッダを利用したほうが高さを抑えることができます。

![img_4134](https://user-images.githubusercontent.com/736191/41305254-53bc4522-6ead-11e8-83ed-c4c7c2787828.png)

下記はOLEDに利用するピンヘッダの比較となります。遊舎工房で購入可能なOLEDは左のように若干低くなっています。

![img_4137](https://user-images.githubusercontent.com/736191/41305263-57e53dac-6ead-11e8-9b5d-5667bca5599e.png)

### 動作確認

キースイッチを付けると何か問題があった場合に修正が難しくなるため、ProMicroとOLEDモジュールを付けた段階で動作確認をすることをおすすめします。

動作確認をする場合は先に下記の「ファームウェア」の章を参考にしてcrkbd用のファームウェアをProMicroに入れてください。

![image](https://user-images.githubusercontent.com/736191/40888832-0d793c3a-6798-11e8-93b4-55ec7e180748.png)

デフォルトのキーマップを適用するとOLEDに押したキーに関する情報が表示されます。ピンセット等でスイッチ部分をショートさせることで動作確認ができます。

LEDを実装した場合はすべて点灯することを確認します。

![image](https://user-images.githubusercontent.com/736191/40888868-73028d36-6798-11e8-8246-0c9ca32711d6.png)

### キースイッチおよびトッププレート

キースイッチとPCBの間にトッププレートを挟んで表面に実装します。

![image](https://user-images.githubusercontent.com/736191/40888597-8a5bf7a0-6794-11e8-89e2-535c3f8381b9.png)

### ボトムプレート

ロープロの場合は4.5mmのスペーサー、それ以外は7.5mmのスペーサーを取り付けたあとにボトムプレートを取り付けます。
またクッションゴムを6つ付けます。

![image](https://user-images.githubusercontent.com/736191/40888724-2892c24a-6796-11e8-8f38-a0a3d5e5440e.png)

### キーキャップ

最後にキーキャップを付けて実装は完了です。

![lrg_dsc03895](https://user-images.githubusercontent.com/736191/40888756-c371e264-6796-11e8-8fc5-e842e8baf2b8.png)

## ファームウェア

下記を参照しファームウェアをProMicroに書き込みます。\
<https://github.com/foostan/crkbd/blob/master/doc/firmware_jp.md>

以上で完成です。
