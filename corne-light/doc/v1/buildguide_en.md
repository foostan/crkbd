# Build Guide

This is the Corne Light v1 build guide.

## Parts

<table>
<thead>
  <tr> <td width = "30%"> Name </td> <td width = "15%"> Count </td> <td> Remarks </td> </tr>
</header>
<tbody>
  <tr>
    <td> PCB </td>
    <td> 1 set </td>
    <td>
      ![PCB](https://user-images.githubusercontent.com/736191/69554623-6be02300-0fe5-11ea-879d-9e4316df0226.JPG)
    </td>
  </tr>
  <tr>
    <td> Top plate </td>
    <td> 2 sheets </td>
    <td>
      ![top-plates](https://user-images.githubusercontent.com/736191/69554621-6be02300-0fe5-11ea-9ca2-5556f99fa2e5.JPG)
    </td>
  </tr>
  <tr>
    <td> Bottom plate </td>
    <td> 2 sheets </td>
    <td rowspan = "2">
      ![bottom-plates](https://user-images.githubusercontent.com/736191/69554622-6be02300-0fe5-11ea-8803-a1c97aae0433.JPG)
    </td>
  </tr>
  <tr>
    <td> ProMicro protective plate </td>
    <td> 2 sheets </td>
  </tr>
  <tr>
    <td> diode </td>
    <td> 42 </td>
    <td>
      ![diodes](https://user-images.githubusercontent.com/736191/69554619-6b478c80-0fe5-11ea-9a26-96d617f2b0f6.JPG)
    </td>
  </tr>
  <tr>
    <td> Spacer M2 7.5mm </td>
    <td> 10 </td>
    <td rowspan = "3">
      ![screws](https://user-images.githubusercontent.com/736191/69554618-6b478c80-0fe5-11ea-8090-b14d989e9d07.JPG)
    </td>
  </tr>
  <tr>
    <td> Spacer M2 9mm </td>
    <td> 4 </td>
  </tr>
  <tr>
    <td> Screw M2 4mm </td>
    <td> 28 </td>
  </tr>
  <tr>
    <td> TRRS jack </td>
    <td> 2 </td>
    <td rowspan = "3">
      ![jacks](https://user-images.githubusercontent.com/736191/69554620-6be02300-0fe5-11ea-94ee-6f8f50d800da.JPG)
    </td>
  </tr>
  <tr>
    <td> Reset switch </td>
    <td> 2 </td>
  </tr>
  <tr>
    <td> Rubber feet </td>
    <td> 8 </td>
  </tr>
  <tr>
    <td> ProMicro (with conthrough) </td>
    <td> 2 </td>
    <td>
      <a href="https://yushakobo.jp/shop/promicro-spring-pinheader/"> https://yushakobo.jp/shop/promicro-spring-pinheader/ </a>
    </td>
  </tr>
  <tr>
    <td> OLED module (with pin socket) </td>
    <td> 2 </td>
    <td>
      <a href="https://yushakobo.jp/shop/oled/"> https://yushakobo.jp/shop/oled/ </a>
    </td>
  </tr>
  <tr>
    <td> key switch </td>
    <td> 42 </td>
    <td> </td>
  </tr>
  <tr>
    <td> keycap </td>
    <td> 42 </td>
    <td> </td>
  </tr>
  <tr>
    <td> TRRS cable </td>
    <td> 1 </td>
    <td> TRS cable is also acceptable </td>
  </tr>
  <tr>
    <td> USB cable </td>
    <td> 1 </td>
    <td> </td>
  </tr>
</tbody>
</table>

## Advance preparation

If you build the firmware yourself,
it takes time to prepare the environment,
so it is recommended to start first. \
See <https://github.com/foostan/crkbd/blob/master/doc/firmware_en.md>
for more information.

## Implementation

### PCB disconnection

Check the front and back and separate the left and right PCBs
(the photo is the front).

![assembly-pcb](https://user-images.githubusercontent.com/736191/69554624-6c78b980-0fe5-11ea-9828-3be0af9f27af.JPG)

This is a jig for bending the legs of a diode.
Separate it if necessary.

![assembly-tool-of-diodes](https://user-images.githubusercontent.com/736191/69554626-6c78b980-0fe5-11ea-8c4d-ae70374d54bc.JPG)

* Some versions do not have a jig.

### Diodes

First, bend the legs of the reed type diode.

* You can clean it by bending it one by one as shown in the picture,
  but it is more efficient to bend multiple pieces at the same time
  while connected to the tape.

![assembly-diodes-1](https://user-images.githubusercontent.com/736191/69554627-6c78b980-0fe5-11ea-9f4f-120c28b49953.JPG)

Attach the diode with the bent leg to the specified position.

![assembly-diodes-2](https://user-images.githubusercontent.com/736191/69554628-6d115000-0fe5-11ea-8885-e88b5d87a3b1.JPG)

The diode has an orientation and is installed as shown in the photo.

* All the diodes to be attached are in the same orientation.

![assembly-diodes-3](https://user-images.githubusercontent.com/736191/69554629-6d115000-0fe5-11ea-9df5-70e8ab10489f.JPG)

You can attach it neatly by fixing it with masking tape.

![assembly-diodes-4](https://user-images.githubusercontent.com/736191/69554632-6d115000-0fe5-11ea-907f-2188aa59094a.JPG)

Solder from the back side.

![assembly-diodes-5](https://user-images.githubusercontent.com/736191/69554633-6da9e680-0fe5-11ea-9d5c-751595784d84.JPG)

If you are fixing with masking tape,
cutting your legs to the limit like this will make soldering easier.

![assembly-diodes-6](https://user-images.githubusercontent.com/736191/69554634-6da9e680-0fe5-11ea-9051-93f9edd09c9a.JPG)

With 21 one-handed and two-handed he installs 42 diodes.

![assembly-diodes-7](https://user-images.githubusercontent.com/736191/69554635-6da9e680-0fe5-11ea-9ee3-b503bc0fcc83.JPG)

### TRRS jack, reset switch, pin socket

Install in the specified position.

* Install the right hand side in the same position
  (be careful of mistakes on the front and back).

![assembly-jacks-resets-pinsockets-1](https://user-images.githubusercontent.com/736191/69554641-6e427d00-0fe5-11ea-87d7-c46056e4fb09.JPG)

### ProMicro, OLED module

Install his ProMicro and his OLED module by referring to the [Helix Build Guide](
https://github.com/MakotoKurauchi/helix/blob/master/Doc/buildguide_en.md#pro-micro).

![assembly-promicro-oled](https://user-images.githubusercontent.com/736191/69554644-6e427d00-0fe5-11ea-8c6b-9aaa3d2c3f6c.JPG)

### Firmware

Write the firmware to ProMicro by referring to the following. \
<https://github.com/foostan/crkbd/blob/master/doc/firmware_en.md>

### Operation check

To check the operation,
connect the left hand side to the PC with a USB cable,
and connect the left hand side and the right hand side with the TRRS cable.
Since there may be defects such as jacks,
be sure to connect the left and right instead of one by one
before checking the operation.

* Since the switch is not attached,
  check the operation with tweezers as shown in the photo.

![check](https://user-images.githubusercontent.com/736191/69554646-6edb1380-0fe5-11ea-8428-afd7bef09c15.JPG)

### Top plate, key switch

Attach the key switch to the top plate as shown in the picture.

* Be careful of the direction of the key switch.

![assembly-keyswitches-1](https://user-images.githubusercontent.com/736191/69554647-6edb1380-0fe5-11ea-9e17-d4d644f9a60c.JPG)

We recommend using a 3-pin key switch.

* Even when using 5 pins, the plastic legs can be separated to make 3 pins.

![assembly-keyswitches-2](https://user-images.githubusercontent.com/736191/69554648-6edb1380-0fe5-11ea-94fe-cd758f46cfd0.JPG)

Solder so that there is no gap between the switch and the PCB.

![assembly-keyswitches-3](https://user-images.githubusercontent.com/736191/69554652-700c4080-0fe5-11ea-8633-afae5e825d02.JPG)
![assembly-keyswitches-4](https://user-images.githubusercontent.com/736191/69554654-700c4080-0fe5-11ea-8514-9a46ba4da38c.JPG)

### ProMicro Protective Plate, Bottom Plate

Attach his ProMicro protective plate using an M2 9mm spacer.

![assembly-plates-1](https://user-images.githubusercontent.com/736191/69554656-700c4080-0fe5-11ea-8083-b55fea60adc9.JPG)

Install the bottom plate using the M2 7.5mm spacer.

![assembly-plates-2](https://user-images.githubusercontent.com/736191/69554660-70a4d700-0fe5-11ea-9c46-eb32c7589470.JPG)

Attach the rubber feet to the four corners.

![assembly-plates-3](https://user-images.githubusercontent.com/736191/69554661-70a4d700-0fe5-11ea-85c1-acae90ea7725.JPG)

## Complete

Attach the keycap and you're done.

![assembly-finished-1](https://user-images.githubusercontent.com/736191/69654854-d615c800-10b8-11ea-8903-ebf019d7b125.png)
![assembly-finished-2](https://user-images.githubusercontent.com/736191/69654882-df069980-10b8-11ea-8efe-069b68db3bc0.png)
