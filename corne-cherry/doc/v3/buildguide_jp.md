# Build Guide

こちらは Corne Cherry v3 のビルドガイドになります。
[Corne Cherry v2 はこちら](https://github.com/foostan/crkbd/blob/master/corne-cherry/doc/v2/buildguide_jp.md)。


## 部品
### 必須
| 名前 | 数 | 備考 | 
|:-|:-|:-|
| PCB | 1セット | |
| トッププレート | 2枚 | |
| ボトムプレート | 2枚 | |
| OLED保護プレート | 2枚 | |
| ProMicro | 2枚 | |
| TRRSジャック | 2個 | |
| タクトスイッチ | 2個 | |
| ダイオード | 42本 | SMD部品のみ対応 |
| PCBソケット | 42個 | Kailh および Gateron に対応 |
| キースイッチ | 42個 | CherryMX互換のみ対応 |
| キーキャップ | 42個 | 1u 40個、1.5u 2個 |
| スペーサー M2 6.5mm | 10本 | |
| スペーサー M2 8mm | 4本 | |
| ネジ M2 4mm | 28本 | |
| クッションゴム | 8個 | |
| TRRS(4極)ケーブル | 1本 | TRS(3極)ケーブルでも可 |
| Micro USBケーブル | 1本 | |

### オプション
| 名前 | 数 | 備考 |
|:-|:-|:-|
| OLEDモジュール | 2枚 | |
| OLEDモジュール用ピンヘッダ 4連 1.5mm | 2つ | |
| OLEDモジュール用ピンソケット 4連 2.5mm | 2つ | |
| YS-SK6812MINI-E | 42個 | Back light用 LEDs |
| WS2812B | 12個 | Undergrow 用 LEDs |

## 事前準備
組み立ての途中で ProMicro にファームウェアを入れる作業がありますが、ファームウェアをビルドする環境を整備するのには時間がかかるためはじめに取り掛かっておくことをおすすめします。

https://docs.qmk.fm/#/ja/newbs_getting_started を参考にし、OSに合わせて必要なものをインストールしておきます。
インストールに時間がかかるため動かしつつ組み立てを進めると効率的です。

## 確認

Corne Cherry v3 のPCBは以下のものになります。お手持ちのPCBと同一のものかご確認ください。

![confirm_front](assets/confirm_front.jpg)

![confirm_back](assets/confirm_back.jpg)

PCBは製造の都合上フレームが付いた状態となっています。
手で折って外すことができますが、難しい場合は接合部分※にカッター等で切り込みを入れると外しやすくなります。
また、接合部分はヤスリ等できれいにすることができます。

※ 接合部分: 下記画像の赤で記した部分のこと、計8箇所あります

![confirm_remove_frame](assets/confirm_remove_frame.jpg)

## 組み立て
### ダイオード

SMD部品のダイオードのはんだづけを行います。
SMD部品は非常に小さいためピンセット及び逆作用ピンセットがあると便利です。

**ダイオードは取り付ける向きが決まっていて**、部品の「|」印が、ダイオードマーク「|◁」の「|」の方に向けるようにはんだづけを行います。
なお、Corne の PCB はダイオードの取り付け向きがすべて統一されています。

![build_diode](assets/build_diode.jpg)

<details>
<summary>TIPS: SMD部品を取り付けるコツ</summary>

SMD部品を取り付けるコツですが、まずは予備ハンダとしてパットの片側のみにハンダを盛ります。

![tips_building_smd_01](https://user-images.githubusercontent.com/736191/54487435-79330280-48d9-11e9-9138-525d8ee68144.jpg)

次に予備ハンダを溶かすようにしてダイオードの片足をはんだ付けします。
このとき、逆作用ピンセットを利用すると力を入れずともチップ部品をしっかりと持つことができ、位置合わせとはんだづけに集中できるのでおすすめです。
またはんだごてがあつすぎたり、はんだを触りすぎたりするとはんだに含まれるフラックスが気化してきれいにはんだの山ができることがありますが、あとで修復できるのでこの時点ではパーツを付けることだけを意識すれば大丈夫です。

![tips_building_smd_02](https://user-images.githubusercontent.com/736191/54487436-79330280-48d9-11e9-856e-f3f5b9f58414.jpg)

片足をつけた段階で横から見てダイオードが浮いていなければ大丈夫です。浮いてしまった場合はダイオードをピンセットや指で押さえつけながらはんだごてではんだづけした部分を再度熱すればきれいになります。

![tips_building_smd_03](https://user-images.githubusercontent.com/736191/54487437-79330280-48d9-11e9-996d-a578e767c12c.jpg)

次にもう片方をはんだづけします。少量のはんだで十分なのでつけすぎに注意します。
つけすぎてしまった場合は吸い取り線で取るか、はんだごてですくうようにすれば取れます。

また予備はんだ側のはんだの量が少ない場合は追加ではんだづけを重ねて行い、山になっている場合はフラックスを上から塗って熱すればきれいになります。

![tips_building_smd_04](https://user-images.githubusercontent.com/736191/54487438-79cb9900-48d9-11e9-9280-dc72a2087307.jpg)

</details>

左右合わせて42個をはんだづけしてダイオードは完了です。

![build_diode_overview](assets/build_diode_overview.jpg)

### LED（オプション）

YS-SK6812MINI-E と WS2812B をはんだづけします。

先に取り付け後の様子を確認しておきます。

![build_led_front_overview](assets/build_led_front_overview.jpg)

はんだづけはすべて裏側から行いますが、YS-SK6812MINI-E は Backlight (表側を光らせる)用、WS2812B は Undergrow (裏側を光らせる)用になっています。
![build_led_back_overview](assets/build_led_back_overview.jpg)

#### WS2812B (Undergrow)

まずは WS2812B をはんだづけします。

下記のように WS2812B の凹みの角とPCBの角印が合う向きにしてはんだづけを行います。
__TIPS: SMD部品を取り付けるコツ__ で紹介したように、予備ハンダをするとうまくつけられると思います。

なお、Corne の PCB は WS2812B の取り付け向きがすべて統一されています。

![build_led_undergrow](assets/build_led_undergrow.jpg)

左右合わせて計8個はんだづけして WS2812B は完了です。

![build_led_undergrow_overview](assets/build_led_undergrow_overview.jpg)

#### YS-SK6812MINI-E (Backlight)

続いて YS-SK6812MINI-E をはんだづけします。

下記のように YS-SK6812MINI-E の角が欠けた足とPCBの角印が合う向きにしてはんだづけを行います。
__TIPS: SMD部品を取り付けるコツ__ で紹介したように、予備ハンダをするとうまくつけられると思います。
SK6812MINI に比べて壊れにくいですが、はんだごての熱を直接受けると破損する可能性があります。温調機能のついたはんだごてで 320℃ ほどであれば、4つの足を連続にはんだづけしても問題なさそうでした。

なお、Corne の PCB は YS-SK6812MINI-E の取り付け向きがすべて統一されています。

![build_led_backlight](assets/build_led_backlight.jpg)


左右合わせて計42個はんだづけして YS-SK6812MINI-E は完了です。

![build_led_back_overview](assets/build_led_back_overview.jpg)

### TRRSジャック、リセットスイッチ、OLED用ピンソケット

下記の写真通りにTRRSジャック、リセットスイッチ(タクトスイッチ)、OLED用ピンソケットをはんだづけします。

![build_trrs_reset_oled](assets/build_trrs_reset_oled.jpg)

ずれやすい部品なので、手で部品を抑えながらはんだづけするか、マスキングテープ等で固定してからはんだづけするときれいに付きます。

### ProMicro
ProMicroを下記のような向きではんだ付けします

![build_promicro](assets/build_promicro.jpg)

なお、コンスルーを利用する場合は裏側のはんだ付けをする必要はありません。
コンスルーの詳しい利用方法は [Helix のビルドガイド](https://github.com/MakotoKurauchi/helix/blob/master/Doc/buildguide_jp.md#pro-micro)をご参照ください。

![build_promicro_conthrough](assets/build_promicro_conthrough.jpg)

### OLEDモジュール
OLED用のピンソケットにピンヘッダを先に差し込み、その後からピンヘッダとOLEDモジュールをはんだづけします。
このときOLEDモジュールが浮きやすいので指で押さえつけながら浮かないように気をつけます。

![build_oled](assets/build_oled.jpg)

### ファームウェア
https://docs.qmk.fm/#/ja/newbs_getting_started こちら等を参考にし、OSに合わせて必要なものをインストールしておきます。
上記の事前準備にも挙げたとおり、インストールに時間がかかるため事前に用意しておくことをおすすめします。

Corne 用のファームウェアは `keyboards/crkbd` です。
なお、LEDはデフォルトでは無効になっているため、`keyboards/crkbd/rules.mk` にて `RGBLIGHT_ENABLE = yes` と変更する必要があります。

```diff
diff --git a/keyboards/crkbd/rules.mk b/keyboards/crkbd/rules.mk
index 30de5b388..174dd5c7e 100644
--- a/keyboards/crkbd/rules.mk
+++ b/keyboards/crkbd/rules.mk
@@ -26,7 +26,7 @@ MIDI_ENABLE = no            # MIDI controls
 AUDIO_ENABLE = no           # Audio output on port C6
 UNICODE_ENABLE = no         # Unicode
 BLUETOOTH_ENABLE = no       # Enable Bluetooth with the Adafruit EZ-Key HID
-RGBLIGHT_ENABLE = no       # Enable WS2812 RGB underlight.
+RGBLIGHT_ENABLE = yes       # Enable WS2812 RGB underlight.

 # Do not enable SLEEP_LED_ENABLE. it uses the same timer as BACKLIGHT_ENABLE
 SLEEP_LED_ENABLE = no    # Breathing sleep LED during USB suspend
```

環境ができたら、下記コマンドでファームウェアをビルドします。

```bash
make crkbd:default
```

ビルドが完了したら下記コマンドを実行します。

```bash
make crkbd:default:avrdude
```

実行すると下記のようなログがでて、`.` が増えていくことが確認出来ると思います。
この間にリセットスイッチを **2回** 押すとファームウェアの書き込みが完了します。

```bash
<省略>

Checking file size of crkbd_rev1_default.hex                                                        [OK]
 * File size is fine - 27328/28672
Copying crkbd_rev1_default.hex to qmk_firmware folder                                               [OK]
Detecting USB port, reset your controller now........
```

片側のProMicroにファームウェアの書き込みが完了したら、もう片方も同じ手順で書き込みを行います。

### 動作確認
ProMicroとOLEDモジュールを付けた段階で動作確認をすることをおすすめします。
一番最後にやると問題の切り分けが難しくなります。

動作確認は左手側はMicroUSBでPCとつなぎ、左手側と右手側をTRRSケーブルで接続させて行います。ジャック等の不良等もありえるので、片方ずつではなく必ず左右を接続させてから動作確認をしてください。ここまで正しくできていれば、PCBソケットを取り付けるパットをピンセット等でショートさせるとOLEDモジュールに押されたキーが表示されます。

### PCBソケット

PCBソケットを下記のようにマークに合わせてはんだづけします。
下記ではすべてのPCBソケットが並んでいますが、しっかりハマるものではないので、1つずつ付けてください。
__TIPS: SMD部品を取り付けるコツ__ で紹介したように、予備ハンダをするとうまくつけられると思います。

![build_socket](assets/build_socket.jpg)

左右合わせて計42個はんだづけしてPCBソケットは完了です。

![build_socket_overview](assets/build_socket_overview.jpg)

### OLED保護プレート

M2 8mm のスペーサーと M2 ネジで OLED 保護プレートを取り付けます。

![build_oled_plate_front](assets/build_oled_plate_front.jpg)
![build_oled_plate_back](assets/build_oled_plate_back.jpg)

### プレート、スイッチ

トッププレートにキースイッチに取り付けた後、キースイッチをソケットにはめ込みます。
先にすべてのキースイッチをトッププレートに取り付けてしまうと、ソケットにはめ込む難易度が上がってしまうため、先に端のキースイッチのみを取り付ける方が簡単です。
![build_top_plate_switches](assets/build_top_plate_switches.jpg)

M2 6.5mm のスペーサーと M2 ネジ をトッププレートに取り付けます。

![build_screws_spacers_front](assets/build_screws_spacers_front.jpg)

裏側からスペーサーを穴に入れた後、ネジ止めをすると簡単です。

![build_screws_spacers_back](assets/build_screws_spacers_back.jpg)

ボトムプレートを M2 ネジで取り付けます。

![build_bottom_plate](assets/build_bottom_plate.jpg)

クッションゴムを以下の位置に取り付けます。

![build_cushion_rubbers](assets/build_cushion_rubbers.jpg)

以上で完成です。

![build_finish](assets/build_finish.jpg)
