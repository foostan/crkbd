# STM32G0B1 左右半二重通信

回路図と Cherry PCB の左右通信を USART1 半二重へ変更した。

- 左右とも PB6（pin 30、USART1_TX / AF0）を送受信に使用。PB7（pin 31）は未接続。
- 回路図の TX / TR ラベルを SERIAL に統一。
- PB6 → U4 pin 4 / pin 3 → J3 の D+（A6 / B6）→ ケーブル → 相手側の同じ端子 → 相手 PB6。
- U4 のもう一方の保護チャネルはコネクタ D− 側の接続を維持し、MCU 側 pin 6 を未接続にした。
- R10 / rR10：各側の 3.3 V へ 4.7 kΩ のプルアップ。両側が給電されている場合、合成抵抗は約 2.35 kΩ。
- 採用品：UNI-ROYAL 0402WGF4701TCE、0402、1%、[JLCPCB C25900](https://jlcpcb.com/partdetail/26643-0402WGF4701TCE/C25900)。BOM 用フィールドは非表示。
- 新しい抵抗の PCB 配置は暫定位置。配置時は MCU / ESD 保護間の SERIAL 配線の近くへ移動する。

## QMK 側の設定

このリポジトリには今回の STM32 用 QMK ターゲットがないため、以下は移植時に反映する設定。コンパイル・実機通信確認は未実施。

`rules.mk`:

```make
SERIAL_DRIVER = usart
```

`config.h`:

```c
#define SERIAL_USART_TX_PIN B6
#define SERIAL_USART_TX_PAL_MODE 0
```

`SERIAL_USART_FULL_DUPLEX` と `SERIAL_USART_PIN_SWAP` は定義しない。受信専用の `SERIAL_USART_RX_PIN` も不要。USART1 を有効にする HAL / MCU 設定と `SERIAL_USART_DRIVER` は、使用する QMK / ChibiOS の STM32G0B1 ターゲットが採用する SERIAL または SIO サブシステムに合わせる。

[QMK 公式半二重ドライバ仕様](https://docs.qmk.fm/drivers/serial#usart-half-duplex)に従い、TX ピンをオープンドレインの送受信兼用にする。通常のプッシュプル UART 出力同士として動かさない。

## 検証

- ERC：エラー 0 / 警告 0（既存プロジェクトのチェック設定）。
- エクスポートしたネットリストで左右の PB6、ESD pin 4、プルアップ抵抗が同一 SERIAL ネットにあることを確認。
- PB7 の未接続、プルアップの 3.3 V 接続を確認。
- PCB ファイルの読み込みを確認。既存配置は維持し、追加抵抗のみ暫定配置。
- 実際に使うケーブルと通信速度で波形・通信エラー・起動時の挙動を確認する。プルアップによる立ち上がり時間はケーブル容量にも依存する。
