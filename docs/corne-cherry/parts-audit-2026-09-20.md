# crkbd 部品・在庫確認（2026-09-20）

対象は現在の `pcbs/common/left.kicad_sch` / `right.kicad_sch` と Cherry 基板。左右一組は実装部品 134 個。基板分離タブ 8 個は購入部品ではないため BOM / 座標出力から除外した。キーキャップと、ソケットへ挿すキースイッチはこの実装 BOM に含めない。

在庫数は 2026-09-20 に JLCPCB の画面で確認した表示値。注文予約ではなく、歩留まり分・実装ロスを含まない。「十分」は通常の小ロットに対しての評価で、製造数量未指定のため必要数の確保は保証しない。Pre-order は表示在庫があっても即時実装可能とは扱わない。

| 参照（r 側も同じ） | 個数/左右組 | 採用品・仕様 | JLCPCB | 表示在庫 | 判定 |
|---|---:|---|---|---:|---|
| SD1 | 2 | Nexperia PMEG4010CEJ,115、40 V / 1 A、SOD-323F | [C50704](https://jlcpcb.com/partdetail/PMEG4010CEJ%2C115/C50704) | 3,410 | 小型化の指示により再変更 |
| D1–D23 | 46 | TWGMC 1N4148WS、SOD-323 | [C727111](https://jlcpcb.com/partdetail/TWGMC-1N4148WS/C727111) | 739,779 | 十分。mrkbd と同じ選定 |
| SW1–SW23 | 46 | HanElectricity CPG151101S11-16、MX ホットスワップソケット | [C41430893](https://jlcpcb.com/partdetail/HanElectricity-CPG151101S1116/C41430893) | 292,051 | 十分。今回選定 |
| U1 | 2 | ST STM32G0B1KBU6、UFQFPN-32、5×5 mm | [C5159549](https://jlcpcb.com/partdetail/STMicroelectronics-STM32G0B1KBU6/C5159549) | 68 | **少ない・Pre-order**。維持 |
| U2 | 2 | TI TPS70933DBVR、3.3 V / 150 mA、SOT-23-5 | [C89347](https://jlcpcb.com/partdetail/TexasInstruments-TPS70933DBVR/C89347) | 793 | **Pre-order**。維持 |
| U3, U4 | 4 | ST USBLC6-2P6、SOT-666 | [C15999](https://jlcpcb.com/partdetail/STMicroelectronics-USBLC62P6/C15999) | 9,659 | 十分。未設定だった品番を追加 |
| J1, J3 | 4 | HRO TYPE-C-31-M-12、USB-C | [C165948](https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M12/C165948) | 117,542 | 十分。型番専用フットプリントと一致 |
| F1, F2 | 4 | LUTE 0603L025/24XR、0603、保持 250 mA / トリップ 550 mA、24 V | [C7472531](https://jlcpcb.com/partdetail/LUTE-0603L025_24XR/C7472531) | 19,406 | 十分。既存 ID に合わせ型番表記を修正 |
| TVSD1, TVSD2 | 4 | Littelfuse SMF5.0A、5 V TVS、SOD-123FL | [C151296](https://jlcpcb.com/partdetail/Littelfuse-SMF50A/C151296) | 42,826 | 十分。既存 D_SOD-123F の選定を維持 |
| BOOT1, NRST1 | 4 | XUNPU TS-1088-AR02016、4×3 mm、高さ 2 mm | [C720477](https://jlcpcb.com/partdetail/XUNPU-TS_1088AR02016/C720477) | 996,012 | 十分。既存実装パターンを維持 |
| R1, R2 | 4 | UNI-ROYAL 0402WGF5101TCE、5.1 kΩ / 1%、0402 | [C25905](https://jlcpcb.com/partdetail/26648-0402WGF5101TCE/C25905) | 6,849,337 | 十分 |
| R8 | 2 | UNI-ROYAL 0402WGF5601TCE、5.6 kΩ / 1%、0402 | [C25908](https://jlcpcb.com/partdetail/26651-0402WGF5601TCE/C25908) | 267,626 | 十分。品番追加 |
| R9 | 2 | UNI-ROYAL 0402WGF1002TCE、10 kΩ / 1%、0402 | [C25744](https://jlcpcb.com/partdetail/26487-0402WGF1002TCE/C25744) | 26,210,599 | 十分。品番追加 |
| C1, C2 | 4 | Samsung CL05B104KO5NNNC、100 nF / 16 V / X7R / 10%、0402 | [C1525](https://jlcpcb.com/partdetail/1877-CL05B104KO5NNNC/C1525) | 28,267,389 | 十分 |
| C6 | 2 | Samsung CL05A105KA5NQNC、1 µF / 25 V / X5R / 10%、0402 | [C52923](https://jlcpcb.com/partdetail/53938-CL05A105KA5NQNC/C52923) | 7,906,766 | 十分 |
| C11 | 2 | Samsung CL10A475KO8NNNC、4.7 µF / 16 V / X5R / 10%、0603 | [C19666](https://jlcpcb.com/partdetail/20375-CL10A475KO8NNNC/C19666) | 3,062,869 | 十分 |

## 変更と照合の根拠

- 電源用は `D24/rD24` から `SD1/rSD1` へ変更。旧 PMEG40T10ER-QX（C5709687）は在庫 8 個しかなく、在庫優先の指示に従い PMEG4010ER,115 に変更した。40 V / 1 A、同じ CFP3 / SOD-123W、1=K・2=A。[Nexperia データシート](https://assets.nexperia.com/documents/data-sheet/PMEG4010ER.pdf)で定格・端子を照合。VF は 25℃・100 mA で最大 0.36 V、1 A で最大 0.49 V。逆漏れは 25℃・10 V で最大 13 µA。供給元の検出用分圧と、PC VBUS から共通電源への向きは維持した。高温を含む検出マージンの実機評価までは行っていない。
- D1–D23 / rD1–rD23 は mrkbd と同じ `Diode:1N4148WS` / `Diode_SMD:D_SOD-323` / C727111 に統一。回路図と Cherry 基板の両方に反映。カソードはパッド 1。
- ソケットは Kailh CPG151101S11（C2803348）と CPG151101S11-16（C5156480）の表示在庫がともに 0。HanElectricity C41430893 を採用した。[メーカー寸法図](https://datasheet.lcsc.com/datasheet/pdf/d953a8b0b623247f3341ebcfbaa2e88f.pdf?productCode=C41430893)の推奨ランド 2.55×2.5 mm、穴径 3.0 mm、穴中心差 X=6.35 / Y=2.54 mm と、既存 1u / 1.5u MX フットプリントを照合した。これはソケットの品番で、キースイッチ本体の品番ではない。Choc 用の選定としては使えない。
- USBLC6-2P6 は ST 純正品の C15999 を選定。SOT-666 と、型番が似ている別パッケージを区別した。
- 抵抗・コンデンサは容量/抵抗値、許容差、定格電圧、誘電体、0402/0603 を照合。PTC は既存 C7472531 に対応するメーカー・正式型番へ表記を合わせた。

## 残る調達上の注意点

1. **MCU は不足しやすい。** 68 個はロスを無視しても左右 34 組分。Pre-order 表示、最小注文数 2。検索結果の KBU6N（C5270168、23 個）、KBU3N（C5270171、11 個）はピン配置の相違があるため、そのまま代用しない。今回 MCU と配線は維持した。
2. **TI レギュレータは事前調達が必要。** C89347 は 793 個表示だが Pre-order、確認時の見積もり 11 日・最小注文数 26。TI の DBVT 品は C2861984、在庫 2・Pre-order で改善しない。TECH PUBLIC / MSKSEMI の類似名製品は TI 品の保証仕様と同一とは確認できないため、自動置換しない。
3. よって **全品が即時調達できる状態ではない**。不足 2 品をそのまま使う場合は発注前に確保が必要。MCU/LDO を在庫豊富な別系列へ変更する場合は、回路・電源仕様・ファームウェアを含む再設計になる。

## 検証範囲

- 現在のプロジェクト設定で回路図 ERC：エラー 0、警告 0。設定で無効なチェックは、単独グローバルラベル・グリッド外端点・4 方向接続・SPICE モデル・フットプリントフィルタ不一致。
- 購入対象の全回路図部品に JLCPCB 品番があること、Cherry 基板との Value / JLCPCB 品番一致を確認。
- 変更前後の全フットプリント位置・角度・面・階層パス・UUID、および番号付きパッドのネット・UUID を比較し、維持を確認。
- PCB DRC はこの環境で CLI が異常終了するため合格確認できていない。基板には旧設計の配置・配線が残っており、今回の部品選定確認を製造可否の判定には使わない。SOD-323 化でパッド形状が変わるため、配線時に再接続・クリアランス確認が必要。
- 共通回路図と Cherry 基板を更新した。Chocolate 基板の実装 BOM / フットプリント同期は対象外。

## SD 小型化の追記

ユーザーの小型化指示により、SD1 / rSD1 を PMEG4010CEJ,115（C50704）、`Diode_SMD:D_SOD-323F` に変更した。上記の PMEG4010ER 選定経緯は変更前の記録。回路図と Cherry 基板を更新し、極性・ネット・位置と管理フィールドの非表示を維持。JLCPCB 表示在庫 3,410 個、注文可能数 3,356 個（2026-09-20 確認）。

40 V / 1 A 定格は維持するが完全同等品ではない。25℃ の VF 最大値は 100 mA で 0.39 V、1 A で 0.57 V。標準 FR4 ランド条件の熱抵抗は 350 K/W。逆漏れ最大値は 40 V・25℃ で 50 µA、5 V の 0.8 µA は代表値であり保証上限ではない。配線・実機評価で発熱および供給元検出のマージンを確認する。[メーカー資料](https://assets.nexperia.com/documents/data-sheet/PMEG4010CEJ.pdf)。今回 TVSD は変更していない。変更後 ERC はエラー 0・警告 0。

## 半二重通信への変更

R10 / rR10 に 4.7 kΩ / 0402 のプルアップ（UNI-ROYAL 0402WGF4701TCE、C25900）を追加。購入部品は左右一組 136 個になった。以前の在庫表にはこの 2 個が含まれていない。詳細は [半二重通信の設計メモ](half-duplex.md) を参照。
