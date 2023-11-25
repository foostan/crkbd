# Build Guide

こちらは Corne Light のビルドガイドになります。

## 部品

<table>
<thead>
  <tr><td width="30%">名前</td><td width="15%">数</td><td>備考</td></tr>
</thead>
<tbody>
  <tr>
    <td>PCB</td>
    <td>1セット</td>
    <td>
      <img alt="PCB" src="https://user-images.githubusercontent.com/736191/69554623-6be02300-0fe5-11ea-879d-9e4316df0226.JPG" width="100%">
    </td>
  </tr>
  <tr>
    <td>トッププレート</td>
    <td>2枚</td>
    <td>
      <img alt="top-plates" src="https://user-images.githubusercontent.com/736191/69554621-6be02300-0fe5-11ea-9ca2-5556f99fa2e5.JPG" width="100%">
    </td>
  </tr>
  <tr>
    <td>ボトムプレート</td>
    <td>2枚</td>
    <td rowspan="2">
      <img alt="bottom-plates" src="https://user-images.githubusercontent.com/736191/69554622-6be02300-0fe5-11ea-8803-a1c97aae0433.JPG" width="100%">
    </td>
  </tr>
  <tr>
    <td>ProMicro保護プレート</td>
    <td>2枚</td>
  </tr>
  <tr>
    <td>ダイオード</td>
    <td>42本</td>
    <td>
      <img alt="diodes" src="https://user-images.githubusercontent.com/736191/69554619-6b478c80-0fe5-11ea-9a26-96d617f2b0f6.JPG" width="100%">
    </td>
  </tr>
  <tr>
    <td>スペーサー M2 7.5mm</td>
    <td>10本</td>
    <td rowspan="3">
      <img alt="screws" src="https://user-images.githubusercontent.com/736191/69554618-6b478c80-0fe5-11ea-8090-b14d989e9d07.JPG" width="100%">
    </td>
  </tr>
  <tr>
    <td>スペーサー M2 9mm</td>
    <td>4本</td>
  </tr>
  <tr>
    <td>ネジ M2 4mm</td>
    <td>28本</td>
  </tr>
  <tr>
    <td>TRRSジャック</td>
    <td>2つ</td>
    <td rowspan="3">
      <img alt="jacks" src="https://user-images.githubusercontent.com/736191/69554620-6be02300-0fe5-11ea-94ee-6f8f50d800da.JPG" width="100%">
    </td>
  </tr>
  <tr>
    <td>リセットスイッチ</td>
    <td>2つ</td>
  </tr>
  <tr>
    <td>ゴム足</td>
    <td>8つ</td>
  </tr>
  <tr>
    <td>ProMicro(コンスルー付き)</td>
    <td>2つ</td>
    <td>
      <a href="https://yushakobo.jp/shop/promicro-spring-pinheader/">https://yushakobo.jp/shop/promicro-spring-pinheader/</a>
    </td>
  </tr>
  <tr>
    <td>OLEDモジュール(ピンソケット付き)</td>
    <td>2つ</td>
    <td>
      <a href="https://yushakobo.jp/shop/oled/">https://yushakobo.jp/shop/oled/</a>
    </td>
  </tr>
  <tr>
    <td>キースイッチ</td>
    <td>42個</td>
    <td></td>
  </tr>
  <tr>
    <td>キーキャップ</td>
    <td>42個</td>
    <td></td>
  </tr>
  <tr>
    <td>TRRSケーブル</td>
    <td>1本</td>
    <td>TRSケーブルでも可</td>
  </tr>
  <tr>
    <td>USBケーブル</td>
    <td>1本</td>
    <td></td>
  </tr>
</tbody>
</table>

## 事前準備

ファームウェアを自分でビルドする場合は環境を整備するのに時間がかかるのではじめに取り掛かっておくことをおすすめします。\
詳しくは <https://github.com/foostan/crkbd/blob/master/doc/firmware_jp.md> を参照してください。

## 実装

### PCBの切り離し

裏表を確認して左右のPCBを切り離します(写真は表です)。

<img alt="assembly-pcb" src="https://user-images.githubusercontent.com/736191/69554624-6c78b980-0fe5-11ea-9828-3be0af9f27af.JPG" width="100%">

こちらはダイオードの足を曲げるための治具です。
必要に応じて切り離しておきます。

<img alt="assembly-tool-of-diodes" src="https://user-images.githubusercontent.com/736191/69554626-6c78b980-0fe5-11ea-8c4d-ae70374d54bc.JPG" width="100%">

※　バージョンによって治具が付いていないものもあります。

### ダイオード

まずはリードタイプのダイオードの足を曲げていきます。
※ 写真のように一本ずつ曲げるときれいにできますが、テープに繋がれたまま複数本を同時に曲げたほうが効率的です。

<img alt="assembly-diodes-1" src="https://user-images.githubusercontent.com/736191/69554627-6c78b980-0fe5-11ea-9f4f-120c28b49953.JPG" width="100%">

足を曲げたダイオードを指定の位置に付けていきます。

<img alt="assembly-diodes-2" src="https://user-images.githubusercontent.com/736191/69554628-6d115000-0fe5-11ea-8885-e88b5d87a3b1.JPG" width="100%">

ダイオードには向きがあり、写真のように取り付けます。
※ 取り付けるダイオードはすべて同じ向きです。

<img alt="assembly-diodes-3" src="https://user-images.githubusercontent.com/736191/69554629-6d115000-0fe5-11ea-9df5-70e8ab10489f.JPG" width="100%">

マスキングテープで固定するときれいに付けることができます。

<img alt="assembly-diodes-4" src="https://user-images.githubusercontent.com/736191/69554632-6d115000-0fe5-11ea-907f-2188aa59094a.JPG" width="100%">

裏面からはんだ付けを行います。

<img alt="assembly-diodes-5" src="https://user-images.githubusercontent.com/736191/69554633-6da9e680-0fe5-11ea-9d5c-751595784d84.JPG" width="100%">

マスキングテープで固定している場合はこのようにギリギリまで足を切るとはんだ付けがやりやすくなります。

<img alt="assembly-diodes-6" src="https://user-images.githubusercontent.com/736191/69554634-6da9e680-0fe5-11ea-9051-93f9edd09c9a.JPG" width="100%">

片手21個、両手分で 42 個のダイオードを取り付けます。

<img alt="assembly-diodes-7" src="https://user-images.githubusercontent.com/736191/69554635-6da9e680-0fe5-11ea-9ee3-b503bc0fcc83.JPG" width="100%">

### TRRSジャック、リセットスイッチ、ピンソケット

指定の位置に取り付けます。
※ 右手側も同じ位置に取り付けます(表裏の間違いに気を付けてください)。

<img alt="assembly-jacks-resets-pinsockets-1" src="https://user-images.githubusercontent.com/736191/69554641-6e427d00-0fe5-11ea-87d7-c46056e4fb09.JPG" width="100%">

### ProMicro、OLEDモジュール

[Helix のビルドガイド](https://github.com/MakotoKurauchi/helix/blob/master/Doc/buildguide_jp.md#pro-micro)を参考にして ProMicro および OLED モジュールを取り付けます。

<img alt="assembly-promicro-oled" src="https://user-images.githubusercontent.com/736191/69554644-6e427d00-0fe5-11ea-8c6b-9aaa3d2c3f6c.JPG" width="100%">

### ファームウェアの書き込み

下記を参照しファームウェアをProMicroに書き込みます。\
<https://github.com/foostan/crkbd/blob/master/doc/firmware_jp.md>

### 動作確認

動作確認は左手側を USB ケーブルで PC とつなぎ、左手側と右手側を TRRS ケーブルで接続して行います。ジャック等の不良もありえるので、片方ずつではなく必ず左右を接続させてから動作確認をしてください。
※ スイッチを付けてないので写真のようにピンセット等で動作確認を行います。

<img alt="check" src="https://user-images.githubusercontent.com/736191/69554646-6edb1380-0fe5-11ea-8428-afd7bef09c15.JPG" width="100%">

### トッププレート、キースイッチ

写真のようにトッププレートにキースイッチをはめます。
※ キースイッチの向きに気を付けてください。

<img alt="assembly-keyswitches-1" src="https://user-images.githubusercontent.com/736191/69554647-6edb1380-0fe5-11ea-9e17-d4d644f9a60c.JPG" width="100%">

キースイッチは3ピンのものをおすすめします。
※ 5ピンを使用する場合でもプラスチックの足を切り離して3ピンにすることができます。

<img alt="assembly-keyswitches-2" src="https://user-images.githubusercontent.com/736191/69554648-6edb1380-0fe5-11ea-94fe-cd758f46cfd0.JPG" width="100%">

スイッチとPCBの間に隙間ができないようにしてはんだ付けを行います。

<img alt="assembly-keyswitches-3" src="https://user-images.githubusercontent.com/736191/69554652-700c4080-0fe5-11ea-8633-afae5e825d02.JPG" width="100%">
<img alt="assembly-keyswitches-4" src="https://user-images.githubusercontent.com/736191/69554654-700c4080-0fe5-11ea-8514-9a46ba4da38c.JPG" width="100%">

### ProMicro 保護プレート、ボトムプレート

M2 9mm スペーサーを用いて ProMicro 保護プレートを取り付けます。

<img alt="assembly-plates-1" src="https://user-images.githubusercontent.com/736191/69554656-700c4080-0fe5-11ea-8083-b55fea60adc9.JPG" width="100%">

M2 7.5mm スペーサーを用いてボトムプレートを取り付けます。

<img alt="assembly-plates-2" src="https://user-images.githubusercontent.com/736191/69554660-70a4d700-0fe5-11ea-9c46-eb32c7589470.JPG" width="100%">

4つ角にゴム足を取り付けます。

<img alt="assembly-plates-3" src="https://user-images.githubusercontent.com/736191/69554661-70a4d700-0fe5-11ea-85c1-acae90ea7725.JPG" width="100%">

## 完成

キーキャップを取り付けて完成です。

<img alt="assembly-finished-1" src="https://user-images.githubusercontent.com/736191/69654854-d615c800-10b8-11ea-8903-ebf019d7b125.png" width="100%">
<img alt="assembly-finished-2" src="https://user-images.githubusercontent.com/736191/69654882-df069980-10b8-11ea-8efe-069b68db3bc0.png" width="100%">

