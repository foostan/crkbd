# ファームウェア
こちらは Corne v1-v3向け(rev1) のファームウェアガイドになります。

## ファームウェアの書き込み

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

![qmk_toolbox_flashed](https://github.com/foostan/crkbd/assets/736191/1a3fdd38-adcd-4c45-82f3-0daf4ef96f4f)

片側にファームウェアの書き込みが完了したら、もう片方も同じ手順で書き込みを行います。

## (オプション) 自分でファームウェアをビルドする場合
こちらを参照してください。https://github.com/foostan/kbd_firmware

## キーマップの変更

[VIA](https://usevia.app/) はVIA用のファームウェアを書き込むことで利用することできます。

![via_begin](https://github.com/foostan/crkbd/assets/736191/ffffab0f-ee66-462b-8266-90214c3551ac)
