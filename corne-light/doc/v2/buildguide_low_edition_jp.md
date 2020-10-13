# Build Guide

こちらは Corne Light v2 Low edition のビルドガイドになります。

![corne-light-low-edition-001](assets/corne-light-low-edition-001.jpg)
![corne-light-low-edition-002](assets/corne-light-low-edition-002.jpg)
![corne-light-low-edition-003](assets/corne-light-low-edition-003.jpg)

## 部品
### 必須
| 名前 | 数 | 備考 | 
|:-|:-|:-|
| PCB | 1セット | |
| トッププレート(アクリル) 2mm | 2枚 | |
| ボトムフォーム | 2枚 | 特殊なフォームを専用の型で切り出しています |
| OLED保護プレート | 2枚 | |
| ProMicro | 2枚 | |
| TRRSジャック | 2個 | |
| タクトスイッチ | 2個 | |
| ダイオード | 42本 | SMD部品推奨 |
| キースイッチ | 42個 | Kailh Choc v1 or v2 推奨 |
| キーキャップ | 42個 | 1u 40個、1.5u 2個 |
| スペーサー M2 8mm | 4本 | |
| ネジ M2 4mm | 8本 | |
| TRRS(4極)ケーブル | 1本 | TRS(3極)ケーブルでも可 |
| Micro USBケーブル | 1本 | |

### オプション
| 名前 | 数 | 備考 |
|:-|:-|:-|
| OLEDモジュール | 2枚 | |
| OLEDモジュール用ピンヘッダ 4連 1.5mm | 2つ | |
| OLEDモジュール用ピンソケット 4連 2.5mm | 2つ | |

## 事前準備
組み立ての途中で ProMicro にファームウェアを入れる作業がありますが、ファームウェアをビルドする環境を整備するのには時間がかかるためはじめに取り掛かっておくことをおすすめします。

https://docs.qmk.fm/#/ja/newbs_getting_started を参考にし、OSに合わせて必要なものをインストールしておきます。
インストールに時間がかかるため動かしつつ組み立てを進めると効率的です。

## 確認

Corne Light v2 のPCBは以下のものになります。お手持ちのPCBと同一のものかご確認ください。

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

### トッププレート、スイッチ

トッププレートにキースイッチに取り付けた後、キースイッチをはんだ付けします。
先にすべてのキースイッチをトッププレートに取り付けてしまうと、スイッチを基板にはめる難易度が上がってしまうため、先に端のキースイッチのみを取り付ける方が簡単です。
![build_top_plate_switches](assets/build_top_plate_switches.jpg)

### OLED保護プレート

M2 8mm のスペーサーと M2 ネジで OLED 保護プレートを取り付けます。

![build_oled_plate_front](assets/build_oled_plate_front.jpg)
![build_oled_plate_back](assets/build_oled_plate_back.jpg)

特に裏側のネジについては、このあとボトムフォームを貼り付けるためしっかりと締めてください。

### ボトムフォーム

最後にボトムフォームを貼り付けます。
このフォームは片側が粘着面、もう片側が滑り止め面になっています。
粘着面をPCBにしっかいと貼り付けてください。

![build_bottom_foam](assets/build_bottom_foam.jpg)

以上で完成です。

![build_finish](assets/build_finish.jpg)

