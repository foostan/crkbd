# Build Guide
こちらは Corne Cherry v4 のビルドガイドになります。

![corne-v4-cherry](https://github.com/foostan/crkbd/assets/736191/c6090d53-67b6-45b5-86c1-1af6214ea392)

## Parts

### Required

| Name                 | Count   | Remarks               |
|:---------------------|:--------|:----------------------|
| PCB                  | 1 set   |                       |
| Case                 | 1 set   |                       |
| Switch plate         | 1 set   | FR4 厚さ 1.6mm          |
| Key switches         | 42 - 46 | Cherry MX 互換のみ        |
| Keycaps              | 42 - 46 | 1u 40 pcs, 1.5u 2 pcs |
| Spacer M2            | 8       | 長さ 7.5 mm             |
| Screw M2             | 16      | 長さ 5 mm               |
| Rubber cushion       | 8       |                       |
| TRRS (4 poles) cable | 1       | TRS (3 poles) は非対応    |
| Type-C cable         | 1       |                       |

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
![plate](https://github.com/foostan/crkbd/assets/736191/75dd4beb-b4fb-4e56-8af3-b4eb736894b7)
![plate-side](https://github.com/foostan/crkbd/assets/736191/ef7cdc65-37f3-4dcc-b5ad-cbbe1440a30d)

### オプション: キースイッチの代わりにロータリーエンコーダをはんだ付けする
ロータリーエンコーダを使う場合、下記の図の位置にキースイッチの代わりにロータリーエンコーダを付けることができます。その場合は、裏側からはんだ付けが必要です。

![rotary-encoder](https://github.com/foostan/crkbd/assets/736191/dd2eb79a-d223-45d2-84fd-331e9f582b5a)

### 2: ケースにスペーサーを付ける
![case](https://github.com/foostan/crkbd/assets/736191/3f295698-29c5-4ed4-9973-3297876a9fc3)

### 3: 1と2を組み合わせる
![switch+case](https://github.com/foostan/crkbd/assets/736191/fd7c2c36-7dea-4c04-a5a5-eee332187a9e)

### 4: ラバークッションを取り付ける
![rubber-cushion](https://github.com/foostan/crkbd/assets/736191/b74e9650-e709-4246-b35d-f8e0b8ebc646)

### 5: キーキャップを取り付ける
![keycap](https://github.com/foostan/crkbd/assets/736191/9a964932-a798-4377-b4c9-59cb2f1bfc5d)
