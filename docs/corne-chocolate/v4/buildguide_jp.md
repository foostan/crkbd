# Build Guide
こちらは Corne Chocolate v4 のビルドガイドになります。

![corne-v4-chocolate](https://github.com/foostan/crkbd/assets/736191/cb352424-9f66-4ad0-9deb-66710e60a781)

## Parts

### Required

| Name                 | Count   | Remarks                     |
|:---------------------|:--------|:----------------------------|
| PCB                  | 1 set   |                             |
| Case                 | 1 set   |                             |
| Switch plate         | 1 set   | FR4 厚さ 1.6mm                |
| Key switches         | 42 - 46 | Kailh choc v1 and v2 スイッチのみ |
| Keycaps              | 42 - 46 | 1u 40 pcs, 1.5u 2 pcs       |
| Spacer M2            | 8       | 長さ 5.5 mm                   |
| Screw M2             | 16      | 長さ 4.5 mm                   |
| Rubber cushion       | 8       |                             |
| TRRS (4 poles) cable | 1       | TRS (3 poles) は非対応          |
| Type-C cable         | 1       |                             |

### Optional

| Name           | Count        | Remarks |
|:---------------|:-------------|:--------|
| Rotary Encoder | 0 - 4 pieces | EC12互換  |

## Firmware preparation

ファームウェアを自分でビルドする場合は環境を整備するのに時間がかかるのではじめに取り掛かっておくことをおすすめします。\
詳しくは [docs/firmware](../../firmware/firmware_jp.md) を参照してください。

## Build
これは左手側のビルドガイドですが、右手側も手順は同じです。

### 1: キースイッチを取り付ける
![plate](https://github.com/foostan/crkbd/assets/736191/c1f87d76-35b6-4aeb-b8c1-26124c8daf27)
![plate-side](https://github.com/foostan/crkbd/assets/736191/781b7c37-877d-4206-aaa6-dac7cd261063)

### オプション: キースイッチの代わりにロータリーエンコーダをはんだ付けする
ロータリーエンコーダを使う場合、下記の図の位置にキースイッチの代わりにロータリーエンコーダを付けることができます。その場合は、裏側からはんだ付けが必要です。

![rotary-encoder](https://github.com/foostan/crkbd/assets/736191/cda08836-46b7-4833-93fe-bcd37a7b9aa7)

### 2: ケースにスペーサーを付ける
![case](https://github.com/foostan/crkbd/assets/736191/3f295698-29c5-4ed4-9973-3297876a9fc3)

### 3: 1と2を組み合わせる
![switch+case](https://github.com/foostan/crkbd/assets/736191/69c56486-54b5-4a95-9d15-6619ade7d521)

### 4: ラバークッションを取り付ける
![rubber-cushion](https://github.com/foostan/crkbd/assets/736191/b74e9650-e709-4246-b35d-f8e0b8ebc646)

### 5: キーキャップを取り付ける
![keycap](https://github.com/foostan/crkbd/assets/736191/58cea8d4-d596-4379-ba91-5d9adb52ecca)
