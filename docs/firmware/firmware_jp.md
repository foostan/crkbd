# ファームウェア

## ファームウェアの書き込み for rev4
VIA用のファームウェアを下記からダウンロードします
- [crkbd_rev4_standard_via.uf2](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_standard_via.uf2)
- [crkbd_rev4_mini_via.uf2](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_mini_via.uf2)

BOOTボタンを押しながらPCに接続するか、PCに接続した状態でBOOTボタンを押しながらリセットボタンを押します。
すると、RPI-PR2デバイスがマウントされます。
![btn](https://github.com/foostan/kbd_firmware/assets/736191/05fd9c4b-12c7-4a32-9606-8fea27bfe7b4)

ダウンロードしたuf2ファイルをRPI-PR2デバイスにドロップすると書き込みが完了します。
![flash](https://github.com/foostan/crkbd/assets/736191/5e5e6eab-3ad3-47f1-9871-1e2bfe554490)

片側にファームウェアの書き込みが完了したら、もう片方も同じ手順で書き込みを行います。

## ファームウェアの書き込み for rev1

### [Remap](https://remap-keys.app/catalog/EfziB9K7ZcxLnIHXl5AQ/firmware) を使う
最も簡単で推奨する方法はRemapを使って crkbd:via を書き込む方法です。
Remapにアクセスし指示に従って書き込みを行ってください。
![flash_by_remap](https://github.com/foostan/kbd_firmware/assets/736191/78b74abe-9853-4a5f-9577-421d39a4a380)

片側にファームウェアの書き込みが完了したら、もう片方も同じ手順で書き込みを行います。

### Flash the firmware by [QMK Toolbox](https://github.com/qmk/qmk_toolbox) を使う

VIA用のファームウェアを [crkbd_rev1_via.hex](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev1_via.hex) からダウンロードします。

QMK Toolbox の 「Open」 からダウンロードしたファイルを指定します。
そしてキーボードをUSBで接続し、リセットボタンを押すとファームウェアの書き込みが始まります。
下記のように書き込みのメッセージが表示されれば完了です。

![qmk_toolbox_flashed](assets/qmk_toolbox_flashed.jpg)

片側にファームウェアの書き込みが完了したら、もう片方も同じ手順で書き込みを行います。

## (オプション) 自分でファームウェアをビルドする場合

[the QMK _getting started_ guide](https://docs.qmk.fm/#/newbs_getting_started) こちらを参照して頂き、ファームウェアを書き込む環境を用意します。

環境ができましたら、下記のファイルを利用して自身でビルドを行ってください。
https://github.com/foostan/kbd_firmware/tree/main/keyboards/crkbd/qmk/qmk_firmware

## キーマップの変更

Corne Keyboardは [VIA](https://usevia.app/) に対応しています。\
VIA用のファームウェアを書き込むことで利用することできます。

### for v4

Corne v4を使う場合は、下記からjsonファイルをダウンロードし、VIAでロードしてください。
- [Corne v4](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/the-via/crkbd_rev4.json)
- [Corne v4 mini](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/the-via/crkbd_rev4_mini.json)

![load_json](https://github.com/foostan/kbd_firmware/assets/736191/67398174-0ef7-4698-9e39-6595b8320428)
![loaded_json](https://github.com/foostan/kbd_firmware/assets/736191/e3e850a8-a5c1-4116-a43d-b2b71c2f606e)
