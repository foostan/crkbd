# ファームウェア
こちらは Corne v4向け(rev4) のファームウェアガイドになります。

## ファームウェアの書き込み
はじめにPCBのバージョンをご確認ください(v4.0.0 または v4.1.0)。\
そしてVIA/Vial用のファームウェアを下記からダウンロードします。

standard (3x6) v4.0.0

- [crkbd_rev4_0_standard_via.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_0_standard_via.uf2)
- [crkbd_rev4_0_standard_vial.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/vial-kb/vial-qmk/.build/crkbd_rev4_0_standard_vial.uf2)

mini (3x5) v4.0.0

- [crkbd_rev4_0_mini_via.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_0_mini_via.uf2)
- [crkbd_rev4_0_mini_vial_mini.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/vial-kb/vial-qmk/.build/crkbd_rev4_0_mini_vial_mini.uf2)

standard (3x6) v4.1.0

- [crkbd_rev4_1_standard_via.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_1_standard_via.uf2)
- [crkbd_rev4_1_standard_vial.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/vial-kb/vial-qmk/.build/crkbd_rev4_1_standard_vial.uf2)

mini (3x5) v4.1.0

- [crkbd_rev4_1_mini_via.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_1_mini_via.uf2)
- [crkbd_rev4_1_mini_vial_mini.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/vial-kb/vial-qmk/.build/crkbd_rev4_1_mini_vial_mini.uf2)

BOOTボタンを押しながらPCに接続するか、PCに接続した状態でBOOTボタンを押しながらリセットボタンを押します。
すると、RPI-PR2デバイスがマウントされます。

![btn](https://github.com/foostan/kbd_firmware/assets/736191/05fd9c4b-12c7-4a32-9606-8fea27bfe7b4)

ダウンロードしたuf2ファイルをRPI-PR2デバイスにドロップすると書き込みが完了します。

![flash](https://github.com/foostan/crkbd/assets/736191/5e5e6eab-3ad3-47f1-9871-1e2bfe554490)

片側にファームウェアの書き込みが完了したら、もう片方も同じ手順で書き込みを行います。

## (オプション) 自分でファームウェアをビルドする場合
こちらを参照してください。https://github.com/foostan/kbd_firmware

## キーマップの変更

### VIA

[VIA](https://usevia.app/) はVIA用のファームウェアを書き込むことで利用することできます。\
Corne v4を使う場合は、下記からjsonファイルをダウンロードし、VIAでロードしてください(設定画面のShow Design tabを有効にする必要があります)。

- [Corne v4](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/the-via/crkbd_rev4.json)
- [Corne v4 mini](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/the-via/crkbd_rev4_mini.json)

![enable_design_tab](https://github.com/foostan/crkbd/assets/736191/fa909532-4151-4190-8820-2ebb7d542517)
![load_json](https://github.com/foostan/kbd_firmware/assets/736191/67398174-0ef7-4698-9e39-6595b8320428)
![loaded_json](https://github.com/foostan/kbd_firmware/assets/736191/e3e850a8-a5c1-4116-a43d-b2b71c2f606e)

### Vial

[Vial](https://vial.rocks/) はVial用のファームウェアを書き込むことで利用することできます。

![Vial](https://github.com/foostan/crkbd/assets/736191/721bd9a3-e832-4322-8cba-1a18622805de)

