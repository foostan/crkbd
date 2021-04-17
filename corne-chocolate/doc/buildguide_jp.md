# Build Guide

こちらは Corne Chocolate のビルドガイドになります。
[Corne Cherry はこちら](https://github.com/foostan/crkbd/blob/master/corne-cherry/doc/buildguide_jp.md)。

## 部品

### 必須

| 名前 | 数 | 備考 |
|:-|:-|:-|
| PCB | 2枚 | |
| トッププレート | 2枚 | |
| ボトムプレート | 2枚 | PCBタイプとアクリルタイプが選べます |
| ProMicro保護プレート | 2枚 | |
| ProMicro | 2枚 | |
| TRRSジャック | 2個 | |
| タクトスイッチ | 2個 | |
| ダイオード | 42本 | チップ部品のみに対応 |
| Kailh PCBソケット(Choc用) | 42個 | |
| キースイッチ | 42個 | Chocにのみ対応 |
| キーキャップ | 42個 | 1u 40個、1.5u 2個 |
| OLEDモジュール | 2枚 | |
| ピンヘッダ 4連 | 2つ | |
| ピンソケット4連 | 2つ | |
| スペーサー M2 4.5mm | 10本 | |
| スペーサー M2 9mm | 4本 | |
| ネジ M2 4mm | 28本 | |
| クッションゴム | 8個 | |
| TRS(3極)ケーブル | 1本 | TRRS(4極)ケーブルでも可 |
| Micro USBケーブル | 1本 | |

### オプション

| 名前 | 数 | 備考 |
|:-|:-|:-|
| SK6812MINI | 54個 | 上向き実装 42個、下向き実装 12個 |

## 事前準備

ファームウェアを自分でビルドする場合は環境を整備するのに時間がかかるのではじめに取り掛かっておくことをおすすめします。\
詳しくは <https://github.com/foostan/crkbd/blob/master/doc/firmware_jp.md> を参照してください。

## 実装

PCBはリバーシブルになっているので、最初にどちらを左用/右用にするか決めます。

![01](https://user-images.githubusercontent.com/736191/52534345-dcce8b00-2d83-11e9-9b6a-b1f9f4b75519.png)

### ダイオード

チップ部品のダイオードのはんだづけを行います。
Corne Cherryではどちらの面に取り付けるかは自由でしたが、Corne Chocolateでは**必ず裏面に取り付けてください**。
表面に実装するとトッププレートと干渉してしまいます。

チップ部品は非常に小さいためピンセット及び逆作用ピンセットがあると作業がしやすくなります。
**ダイオードは取り付ける向きが決まっている**ので、次の写真のように予め取り付ける列と行を揃えて配置しておくとスムーズに進められます。

![02](https://user-images.githubusercontent.com/736191/52534466-1b187a00-2d85-11e9-8ce3-bb13067a1b29.png)

ダイオードの向きは次のとおりです。チップ部品の「|||」印が、ダイオードマーク「|◁」の「|」の方に向けるように取り付けます(画像はCorne Cherryから転記)。

![03](https://user-images.githubusercontent.com/736191/54487560-cb285800-48da-11e9-9e1e-aafaacf5723c.jpg)

チップ部品を取り付けるコツですが、まずは予備ハンダとしてパッドの右側のみにハンダを盛ります。

![04](https://user-images.githubusercontent.com/736191/52534531-0c7e9280-2d86-11e9-9636-ba582cdae265.png)

次に予備ハンダを溶かすようにしてダイオードの片足をはんだ付けします。
このとき、逆作用ピンセットを利用すると力を入れずともチップ部品をしっかりと持つことができ、位置合わせとはんだづけに集中できるのでおすすめです。
またはんだごてがあつすぎたり、はんだを触りすぎたりするとはんだに含まれるフラックスが気化してきれいにはんだの山ができることがありますが、あとで修復できるのでこの時点ではパーツを付けることだけを意識すれば大丈夫です。

![05](https://user-images.githubusercontent.com/736191/52534541-320b9c00-2d86-11e9-982c-45ec7f7b7741.png)

次にもう片方をはんだづけします。少量のはんだで十分なのでつけすぎに注意します。
つけすぎてしまった場合は吸い取り線で取るか、はんだごてですくうようにすれば取れます。

![06](https://user-images.githubusercontent.com/736191/52534553-56677880-2d86-11e9-872e-ea374c8f6824.png)

また予備はんだ側のはんだの量が少ない場合は追加ではんだづけを重ねて行い、山になっている場合はフラックスを上から塗って熱すればきれいになります。

![07](https://user-images.githubusercontent.com/736191/52534577-b78f4c00-2d86-11e9-9c6d-64893dce2754.png)

### TRRSジャック、リセットスイッチ、ピンソケット

![08](https://user-images.githubusercontent.com/736191/52534580-bfe78700-2d86-11e9-9fa6-bdde5283af5b.png)

下記の写真通りにTRRSジャック、リセットスイッチ、ピンソケットをPCBの**表面にはんだづけします**。
ダイオードを裏側につけているので、その反対側の面になります。

![09](https://user-images.githubusercontent.com/736191/52534621-40a68300-2d87-11e9-9749-14459d2b1eac.png)

### OLEDモジュールのためのジャンパ

OLEDモジュールを利用する場合は下記のようにジャンパします。
なお**表面のみジャンパしてください**。

![10](https://user-images.githubusercontent.com/736191/52534622-4d2adb80-2d87-11e9-8935-f7dc5fab4c38.png)

ジャンパがうまくいかない場合はおそらくはんだの量が少ないか、はんだに含まれるフラックスが気化してしまっています。
その場合は、はんだを多めに使うか、別途フラックスを塗るとうまくジャンパができます。

### ProMicro

![11](https://user-images.githubusercontent.com/736191/52534637-99761b80-2d87-11e9-958a-c6ca836a7936.png)

ピンヘッダを白い枠に当てはめるようにはんだづけし、そこにProMicroの裏面を上にしてはんだづけします。

![12](https://user-images.githubusercontent.com/736191/52534641-a266ed00-2d87-11e9-8dcb-832b90556ac2.png)
![13](https://user-images.githubusercontent.com/736191/52534643-aa269180-2d87-11e9-9c05-67924d235968.png)

なおスプリングピンヘッダを利用する場合は [Helix のビルドガイド](https://github.com/MakotoKurauchi/helix/blob/master/Doc/buildguide_jp.md#pro-micro)を参考にしてください。

### OLEDモジュール

![14](https://user-images.githubusercontent.com/736191/52534716-4bade300-2d88-11e9-9fc4-e96787870d07.png)

OLED用のピンソケットにピンヘッダを先に差し込み、その後からピンヘッダとOLEDモジュールをはんだづけします。
このときOLEDモジュールが浮きやすいので指で押さえつけながら浮かないように気をつけます。

![15](https://user-images.githubusercontent.com/736191/52534720-5e281c80-2d88-11e9-9b76-164d9b63692f.png)
![16](https://user-images.githubusercontent.com/736191/52534722-67b18480-2d88-11e9-94d0-e3c899bcc020.png)

### 動作確認

ProMicroとOLEDモジュールを付けた段階で動作確認をすることをおすすめします(一番最後にやると問題の切り分けが難しくなる)。

動作確認をする場合は先に下記の「ファームウェア」の章を参考にしてcrkbd用のファームウェアをProMicroに入れてください（必ず両側に入れてください）。

動作確認は左手側はMicroUSBでPCとつなぎ、左手側と右手側をTRSケーブルで接続させて行います。ジャック等の不良等もありえるので、片方ずつではなく必ず左右を接続させてから動作確認をしてください。ここまで正しくできていれば、PCBソケットを取り付けるパッドをピンセット等でショートさせるとOLEDモジュールに押されたキーが表示されます。

![17](https://user-images.githubusercontent.com/736191/52534757-b95a0f00-2d88-11e9-9a81-467a9efbb935.png)

## LED（オプション）

![18](https://user-images.githubusercontent.com/736191/52534775-fd4d1400-2d88-11e9-8fcc-9916160a6478.png)

SK6812MINIを取り付けていきます。
なお、LEDの取り付けは完成後からでも行えるので、実装が心配な方はこの章を飛ばして、まずは完成させることをおすすめします。

SK6812MINIは非常に熱に弱く、簡単に壊れます。
温調機能がついたはんだごてを利用し、220℃ ~ 270℃ぐらいの温度で作業することをおすすめします。
また温度を調整しても長い時間コテをLEDに当てていると破損するので、なるべくすばやくはんだづけすることを心がけます。
LEDは４つずつはんだづけを行いますが、一度に４つ行わず、２つずつ行ってLEDの温度の上昇を防ぐと破損しづらくなるのでおすすめです。

まずは取り付ける位置の確認です。

1 ~ 6は裏面側(Undergrow)が光るようにし、7 ~ 27は表側（Backlight）が光るようにはんだづけを行います。下記がLEDを取り付ける位置です(画像はCorne Cherryから転記)。

![19](https://user-images.githubusercontent.com/736191/46822561-c6f58d00-cdc6-11e8-90d4-de015410a7a4.png)
![20](https://user-images.githubusercontent.com/736191/46822569-cc52d780-cdc6-11e8-9602-f6265a2c876d.png)

1 ~ 6 は下記のように丸印で囲った黒い部分を下にしたとき、矢印で示したシルクの目印が上になるようにはんだづけを行います。
1 ~ 3 と 4 ~ 5 で向きが変わるので注意してください。

![21](https://user-images.githubusercontent.com/736191/46822428-6d8d5e00-cdc6-11e8-8858-06e8dbdb8ee8.png)

7 ~ 27 は下記のように、丸印で囲った一番大きなパッドと、矢印で示したシルクの目印が隣り合うようにはんだづけを行います。

![22](https://user-images.githubusercontent.com/736191/46822434-6ebe8b00-cdc6-11e8-9686-69ac88bb4389.png)

すべて正常にはんだづけができれば下記のように光ります。
もし途中までしか光らない場合は数字の順番でLEDがつながっているので、光らないLEDもしくはその前のLEDのはんだづけミスやLEDの破損を疑ってください。

![23](https://user-images.githubusercontent.com/736191/52534803-751b3e80-2d89-11e9-9588-75576942ba46.png)
![24](https://user-images.githubusercontent.com/736191/52534807-7c424c80-2d89-11e9-9580-0daffc862ebb.png)
![25](https://user-images.githubusercontent.com/736191/52534811-85331e00-2d89-11e9-9752-c40ffab23419.png)

### Kailh PCBソケット

![26](https://user-images.githubusercontent.com/736191/52534832-be6b8e00-2d89-11e9-82e6-be53dd82bf59.png)

裏面の両側のパッドにはんだを盛ります。後から追加するのが難しいので予め多めに盛ってください。

![27](https://user-images.githubusercontent.com/736191/52534834-c75c5f80-2d89-11e9-987e-d1ca43cf6bc3.png)

ソケットをはめこみ、持ったはんだを溶かすようにして取り付けます。
このときソケットが浮かないようにピンセットや指で押さえつけながら行います。

![28](https://user-images.githubusercontent.com/736191/52534839-d0e5c780-2d89-11e9-8579-d6967b801229.png)

はんだづけはこれで完了です。

![29](https://user-images.githubusercontent.com/736191/52534855-05f21a00-2d8a-11e9-8a63-a9f8b09a730a.png)
![30](https://user-images.githubusercontent.com/736191/52534859-0c809180-2d8a-11e9-959a-83c58da83844.png)

### プレート、スイッチ

![31](https://user-images.githubusercontent.com/736191/52534879-55384a80-2d8a-11e9-9648-e9e9b81625c1.png)

トッププレートとボトムプレート用のスペーサーは4.5mm、OLED用のスペーサーは9mmを使用します。

![32](https://user-images.githubusercontent.com/736191/52534882-67b28400-2d8a-11e9-987d-00b5e14a8f2c.png)

なおプレートの側面を黒のマジックで塗りつぶすと見栄えが良くなるのでおすすめです。

![33](https://user-images.githubusercontent.com/736191/52534914-00e19a80-2d8b-11e9-8005-7e0b157e09e4.png)

## ファームウェア

下記を参照しファームウェアをProMicroに書き込みます。\
<https://github.com/foostan/crkbd/blob/master/doc/firmware_jp.md>

以上で完成です。

![34](https://user-images.githubusercontent.com/736191/52534969-be6c8d80-2d8b-11e9-82ac-a2cd09ab96d1.png)
