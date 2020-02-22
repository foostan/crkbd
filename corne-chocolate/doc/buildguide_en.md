> Translated by Google

# Build Guide

This is the build guide for Corne Chocolate.
[Click here for Corne Cherry] (https://github.com/foostan/crkbd/blob/master/corne-cherry/doc/buildguide_jp.md).

## parts
### required
| Name | Number | Remarks | 
|:-|:-|:-|
| PCB | 2 pieces | |
| Top plate | 2 pieces | |
| Bottom plate | Two pieces | PCB type and acrylic type are available |
| ProMicro protection plate | 2 pieces | |
| ProMicro | 2 | |
| TRRS Jack | 2 | |
| Tact switch | 2 pieces | |
| Diode | 42 pieces | Compatible with chip components only
| Kailh PCB Socket (for Choc) | 42 | |
| Key switch | 42 pieces | Compatible with Choc only |
| Keycaps | 42 | 1u 40, 1.5u 2 |
| OLED module | 2 pieces | |
| 4 pin headers | 2 | |
| 4 pin sockets | 2 | |
| Spacer M2 3.5mm | 10 | |
| Spacer M2 8mm | Four | |
| Screw M2 3mm | 28 | |
| Cushion rubber | 8 pieces | |
| TRS (3 pole) cable | 1 | TRRS (4 pole) cable also available |
| Micro USB Cable | 1 | |

### Option
| Name | Number | Remarks |
|:-|:-|:-|
| SK6812MINI | 54 | Upward mounting 42, Downward mounting 12 |

## Advance preparation
There is work to add a farm to ProMicro in the middle of implementation, but it is time-consuming to prepare the environment for building the farm, so it is recommended to start with it first.
https://docs.qmk.fm/#/newbs_getting_started Refer to here etc. and install the necessary ones according to the OS (it takes time to install, so it is efficient to run while running while proceeding).

## Implementation

Since the PCB is reversible, first decide which one to use for the left or right.

![01](https://user-images.githubusercontent.com/736191/52534345-dcce8b00-2d83-11e9-9b6a-b1f9f4b75519.png)

### diode


Solder the diode of the chip part.
On Corne Cherry it is up to you to choose which side to attach, but with Corne Chocolate you must ** be sure to attach it to the back **.
Mounting on the surface will interfere with the top plate.

Since the chip parts are very small, it is easier to work with tweezers and adverse tweezers.
** Since the mounting direction of the diode is determined **, it is possible to proceed smoothly if you arrange the columns and rows to be mounted in advance as shown in the following photo.

![02](https://user-images.githubusercontent.com/736191/52534466-1b187a00-2d85-11e9-8ce3-bb13067a1b29.png)

The direction of the diode is as follows. Attach the chip component so that the “|||” mark is facing the “|” of the diode mark “| ◁” (image is posted from Corne Cherry).

![03](https://user-images.githubusercontent.com/736191/54487560-cb285800-48da-11e9-9e1e-aafaacf5723c.jpg)

Tips for attaching chip parts, but first put solder only on the right side of the pad as spare solder.

![04](https://user-images.githubusercontent.com/736191/52534531-0c7e9280-2d86-11e9-9636-ba582cdae265.png)

Next, solder one of the diodes by melting the spare solder.
At this time, it is recommended that you use inverted tweezers so that you can hold the chip part firmly without applying force and concentrate on alignment and soldering.
Also, if the soldering iron is too hot or the solder is touched too much, the flux contained in the solder may evaporate and a solder pile may be formed neatly, but since it can be repaired later, at this point just be aware of attaching parts. It's okay.

![05](https://user-images.githubusercontent.com/736191/52534541-320b9c00-2d86-11e9-982c-45ec7f7b7741.png)

Then solder the other. Be careful not to apply too much because a small amount of solder is sufficient.
If you have applied too much, you can remove it with a suction line or scoop it with a soldering iron.

![06](https://user-images.githubusercontent.com/736191/52534553-56677880-2d86-11e9-872e-ea374c8f6824.png)

If the amount of solder on the pre-soldering side is small, perform additional soldering, and if it is peaked, apply flux from above and heat to clean.

![07](https://user-images.githubusercontent.com/736191/52534577-b78f4c00-2d86-11e9-9c6d-64893dce2754.png)

### TRRS jack, reset switch, pin socket

![08](https://user-images.githubusercontent.com/736191/52534580-bfe78700-2d86-11e9-9fa6-bdde5283af5b.png)

Solder the TRRS jack, reset switch and pin socket to the ** surface of the PCB ** as shown in the picture below.
Since the diode is attached on the back side, it will be on the opposite side.

![09](https://user-images.githubusercontent.com/736191/52534621-40a68300-2d87-11e9-9749-14459d2b1eac.png)

### Jumpers for OLED modules
When using OLED module, jumper as follows.
** Please jumper only on the surface **.

![10](https://user-images.githubusercontent.com/736191/52534622-4d2adb80-2d87-11e9-8935-f7dc5fab4c38.png)

If the jumper doesn't work, you probably have a small amount of solder or the flux in the solder has vaporized.
In that case, if you use a lot of solder or apply a separate flux, you can make a jumper well.

### ProMicro

![11](https://user-images.githubusercontent.com/736191/52534637-99761b80-2d87-11e9-958a-c6ca836a7936.png)

Solder the pin header to the white frame and solder the ProMicro back side up.

![12](https://user-images.githubusercontent.com/736191/52534641-a266ed00-2d87-11e9-8dcb-832b90556ac2.png)
![13](https://user-images.githubusercontent.com/736191/52534643-aa269180-2d87-11e9-9c05-67924d235968.png)

When using the spring pin header, please refer to [Helix Build Guide] (https://github.com/MakotoKurauchi/helix/blob/master/Doc/buildguide_jp.md#pro-micro).

### OLED module

![14](https://user-images.githubusercontent.com/736191/52534716-4bade300-2d88-11e9-9fc4-e96787870d07.png)

Insert the pin header into the OLED pin socket first, then solder the pin header and the OLED module.
At this time, be careful not to float the OLED module while holding it down with your finger because it is easy to float.

![15](https://user-images.githubusercontent.com/736191/52534720-5e281c80-2d88-11e9-9b76-164d9b63692f.png)
![16](https://user-images.githubusercontent.com/736191/52534722-67b18480-2d88-11e9-94d0-e3c899bcc020.png)

### Operation check
We recommend that you check the operation at the stage where the ProMicro and OLED modules are attached (it is difficult to isolate the problem at the end).

Before checking the operation, insert the crkbd firmware into ProMicro by referring to the “Firmware” section below (be sure to insert it on both sides).

Operation confirmation is performed by connecting the left hand side to a PC with MicroUSB and connecting the left hand side and the right hand side with a TRS cable. Since there may be a defect such as a jack, make sure to connect the left and right instead of one by one before checking the operation. If you have done this correctly, short-circuit the pad to attach the PCB socket with tweezers etc., and the key pressed on the OLED module will be displayed.

![17](https://user-images.githubusercontent.com/736191/52534757-b95a0f00-2d88-11e9-9a81-467a9efbb935.png)

## LED (optional)

![18](https://user-images.githubusercontent.com/736191/52534775-fd4d1400-2d88-11e9-8fcc-9916160a6478.png)

I will install SK6812MINI.
The LED can be mounted even after completion, so if you are worried about mounting it, we recommend that you skip this chapter and complete it first.

SK6812MINI is very heat sensitive and breaks easily.
We recommend using a soldering iron with a temperature control function and operating at a temperature of about 220 ° C to 270 ° C.
Even if the temperature is adjusted, if the iron is left on the LED for a long time, it will be damaged, so try to solder as quickly as possible.
Solder four LEDs at a time, but we recommend soldering two at a time instead of four at a time to prevent the LED temperature from rising, as this will make it harder to break.

First, check the mounting position.

Solder 1 ~ 6 so that the back side (Undergrow) shines, 7 ~ 27 so that the front side (Backlight) shine. Below is the location to attach the LED (image is posted from Corne Cherry).

![19](https://user-images.githubusercontent.com/736191/46822561-c6f58d00-cdc6-11e8-90d4-de015410a7a4.png)
![20](https://user-images.githubusercontent.com/736191/46822569-cc52d780-cdc6-11e8-9602-f6265a2c876d.png)

For steps 1 to 6, solder the product so that the black part circled below is on the bottom and the silk mark indicated by the arrow is on the top.
Note that the direction changes between 1 ~ 3 and 4 ~ 5.

![21](https://user-images.githubusercontent.com/736191/46822428-6d8d5e00-cdc6-11e8-8858-06e8dbdb8ee8.png)

For 7 to 27, perform soldering so that the largest pad surrounded by a circle and the silk mark indicated by an arrow are adjacent to each other, as shown below.

![22](https://user-images.githubusercontent.com/736191/46822434-6ebe8b00-cdc6-11e8-9686-69ac88bb4389.png)

If everything can be successfully soldered, it will glow as follows.
If the LED lights only halfway, the LEDs are connected in the order of the numbers. Therefore, suspect that the LED that does not emit light or the previous LED is incorrectly soldered or damaged.

![23](https://user-images.githubusercontent.com/736191/52534803-751b3e80-2d89-11e9-9588-75576942ba46.png)
![24](https://user-images.githubusercontent.com/736191/52534807-7c424c80-2d89-11e9-9580-0daffc862ebb.png)
![25](https://user-images.githubusercontent.com/736191/52534811-85331e00-2d89-11e9-9752-c40ffab23419.png)

### Kailh PCB Socket
![26](https://user-images.githubusercontent.com/736191/52534832-be6b8e00-2d89-11e9-82e6-be53dd82bf59.png)

Apply solder to the pads on both sides on the back. It is difficult to add it later, so please fill it up beforehand.

![27](https://user-images.githubusercontent.com/736191/52534834-c75c5f80-2d89-11e9-987e-d1ca43cf6bc3.png)

Insert the socket and melt the solder.
At this time, hold the socket with tweezers or fingers so that the socket does not float.

![28](https://user-images.githubusercontent.com/736191/52534839-d0e5c780-2d89-11e9-8579-d6967b801229.png)

The soldering is now complete.

![29](https://user-images.githubusercontent.com/736191/52534855-05f21a00-2d8a-11e9-8a63-a9f8b09a730a.png)
![30](https://user-images.githubusercontent.com/736191/52534859-0c809180-2d8a-11e9-959a-83c58da83844.png)

### Plate, switch

![31](https://user-images.githubusercontent.com/736191/52534879-55384a80-2d8a-11e9-9648-e9e9b81625c1.png)

Use 3.5mm spacers for the top and bottom plates and 8mm spacers for the OLED.

![32](https://user-images.githubusercontent.com/736191/52534882-67b28400-2d8a-11e9-987d-00b5e14a8f2c.png)

In addition, it is recommended to paint the side of the plate with black magic because it looks better.

![33](https://user-images.githubusercontent.com/736191/52534914-00e19a80-2d8b-11e9-8005-7e0b157e09e4.png)

## Firmware
https://docs.qmk.fm/#/newbs_getting_started See here and prepare the environment to write the firmware.

Once the environment is created, build the firmware for Crkbd with the following command.

`` `
make crkbd: default
`` `

When the build is completed, execute the following command.

`` `
make crkbd: default: avrdude
`` `

When you execute it, you will see the following log, and you can see that `.` increases.
Press the reset switch ** twice ** during this time to complete the firmware writing.

`` `
<Omitted>

Checking file size of crkbd_rev1_default.hex [OK]
 * File size is fine-27328/28672
Copying crkbd_rev1_default.hex to qmk_firmware folder [OK]
Detecting USB port, reset your controller now ........
`` `

Once the firmware has been written to one side of the ProMicro, the other side will follow the same procedure.

This is the end.

! [34] (https://user-images.githubusercontent.com/736191/52534969-be6c8d80-2d8b-11e9-82ac-a2cd09ab96d1.png)


