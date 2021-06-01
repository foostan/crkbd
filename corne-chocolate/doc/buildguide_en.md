# Build Guide

This is the build guide for Corne Chocolate.
[Click here for the Corne Cherry build guide](
https://github.com/foostan/crkbd/blob/master/corne-cherry/doc/buildguide_en.md).

## Parts

### Required

| Name | Count | Remarks |
|:-|:-|:-|
| PCB | 2 pieces | |
| Top plate | 2 pieces | |
| Bottom plate | Two pieces | PCB type and acrylic type are available |
| Pro Micro protection plate | 2 pieces | |
| Pro Micro | 2 | |
| TRRS Jack | 2 | |
| Tactile switch | 2 pieces | |
| Diode | 42 pieces | Compatible with chip components only
| Kailh PCB Socket (for Choc) | 42 | |
| Key switch | 42 pieces | Compatible with Choc (low profile) only |
| Key-caps | 42 | 1u 40, 1.5u 2 |
| OLED module | 2 pieces | |
| 4 pin headers | 2 | |
| 4 pin sockets | 2 | |
| Spacer M2 4.5mm | 10 | |
| Spacer M2 9mm | Four | |
| Screw M2 4mm | 28 | |
| Cushion rubber | 8 pieces | |
| TRS (3 pole) cable | 1 | TRRS (4 pole) cable also available |
| Micro USB Cable | 1 | |

### Optional

| Name | Count | Remarks |
|:-|:-|:-|
| SK6812MINI | 54 | 42 for backlight, 12 for under-glow |

## Advance preparation

If you build the firmware yourself,
it will take some time to set up the environment,
so it's best to start at the beginning. \
For more information,
please see <https://github.com/foostan/crkbd/blob/master/doc/firmware_en.md>.

## Building

Since the PCB is reversible,
you first have to decide which one to use for the left side.

![](https://user-images.githubusercontent.com/736191/52534345-dcce8b00-2d83-11e9-9b6a-b1f9f4b75519.png)

### Diodes

Solder the diodes to the PCB.

On Corne Cherry, it is up to you to choose which side to attach,
but with Corne Chocolate you must **be sure to attach it to the back**.
Mounting on the front will interfere with the top plate.

Since the diodes are very small,
it is easier to work with tweezers and inverted tweezers.
Since the **mounting orientation of the diode is crucial**,
it is possible to proceed smoothly
if you arrange the columns and rows to be mounted in advance,
as shown in the following photo.

![](https://user-images.githubusercontent.com/736191/52534466-1b187a00-2d85-11e9-8ce3-bb13067a1b29.png)

The orientation of the diode is as follows.
Attach the chip component so that the "|||" mark on the diode is facing the "|"
of the diode mark "|◁" on the PCB (image from Corne Cherry).

![](https://user-images.githubusercontent.com/736191/54487560-cb285800-48da-11e9-9e1e-aafaacf5723c.jpg)

Tip for soldering on SMD parts:
First put solder only on the right side of the pad.

![](https://user-images.githubusercontent.com/736191/52534531-0c7e9280-2d86-11e9-9636-ba582cdae265.png)

Next, solder one of the diodes by melting the solder you already put on the board.
At this time,
it is recommended to use [reverse-action tweezers](https://www.alimed.com/_resources/cache/images/product/70895A_850x480-pad.jpg),
so that you can hold the SMD part firmly without applying force,
and concentrate on alignment and soldering instead.
Also, if the soldering iron is too hot or the solder is touched too long,
the flux contained in the solder may evaporate and form an undesirable pile solder,
but since it can be repaired later,
so at this point you should only care about attaching parts.
It's okay.

![](https://user-images.githubusercontent.com/736191/52534541-320b9c00-2d86-11e9-982c-45ec7f7b7741.png)

Then solder the other pin.
Be careful not to apply too much solder,
as a small amount is sufficient.
If you have applied too much,
you can remove it with a suction pump, blotting wire
or by scooping it with a soldering iron.

![](https://user-images.githubusercontent.com/736191/52534553-56677880-2d86-11e9-872e-ea374c8f6824.png)

If the amount of solder on the pre-soldering side is too small,
add more soldering,
and if it is pilled up,
apply flux from above and heat to clean.

![](https://user-images.githubusercontent.com/736191/52534577-b78f4c00-2d86-11e9-9c6d-64893dce2754.png)

### TRRS jack, reset switch, pin socket

![](https://user-images.githubusercontent.com/736191/52534580-bfe78700-2d86-11e9-9fa6-bdde5283af5b.png)

Solder the TRRS jack, reset switch and pin socket to the **front of the PCB**
as shown in the picture below.
Since the diode is attached on the back side,
it will be on the opposite side.

![](https://user-images.githubusercontent.com/736191/52534621-40a68300-2d87-11e9-9749-14459d2b1eac.png)

### Jumpers for OLED modules

When using an OLED module, use solder as jumpers (4 times per side) as follows.
**Please jumper only on the surface**.

![](https://user-images.githubusercontent.com/736191/52534622-4d2adb80-2d87-11e9-8935-f7dc5fab4c38.png)

If the jumper doesn't work,
you probably have a small amount of solder,
or the flux has vaporized.
If so, you can fix the jumper by applying more solder or separate flux.

### Pro Micro

![](https://user-images.githubusercontent.com/736191/52534637-99761b80-2d87-11e9-958a-c6ca836a7936.png)

Solder the pin headers to the white frame
and solder the Pro Micro with back side up.

![](https://user-images.githubusercontent.com/736191/52534641-a266ed00-2d87-11e9-8dcb-832b90556ac2.png)
![](https://user-images.githubusercontent.com/736191/52534643-aa269180-2d87-11e9-9c05-67924d235968.png)

When using the spring-loaded pin headers,
please refer to the [Helix Build Guide](
https://github.com/MakotoKurauchi/helix/blob/master/Doc/buildguide_en.md#pro-micro).

### OLED module

![](https://user-images.githubusercontent.com/736191/52534716-4bade300-2d88-11e9-9fc4-e96787870d07.png)

Insert the pin header into the OLED pin socket first,
then solder the pin header and the OLED module.
At this time,
make sure that the OLED module sits tightly on the socket
while holding it down with your finger,
because it tends to stick out easily.

![](https://user-images.githubusercontent.com/736191/52534720-5e281c80-2d88-11e9-9b76-164d9b63692f.png)
![](https://user-images.githubusercontent.com/736191/52534722-67b18480-2d88-11e9-94d0-e3c899bcc020.png)

### Operation check

We recommend that you check the operation at the stage
where the Pro Micro and OLED modules are attached
(it is difficult to isolate the problem at the end).

Before checking the correct operation,
flash the crkbd firmware to the Pro Micro
by referring to the [Firmware](#firmware) section below
(be sure to insert it on both sides).

Operation confirmation is performed
by connecting the left hand side to a PC with Micro USB
and connecting the left hand side and the right hand side with a TRS cable.
Since there may be a defect such as a jack,
make sure to connect the left and right
instead of one by one before checking the operation.
If you have done this correctly,
short-circuit the pad to attach the PCB socket with tweezers,
and the key pressed on the OLED module will be displayed.

![](https://user-images.githubusercontent.com/736191/52534757-b95a0f00-2d88-11e9-9a81-467a9efbb935.png)

## LED (optional)

![](https://user-images.githubusercontent.com/736191/52534775-fd4d1400-2d88-11e9-8fcc-9916160a6478.png)

I will install SK6812MINI.
The LED can be mounted even after completion,
so if you are worried about mounting it,
we recommend that you skip this chapter and complete it first.

SK6812MINI is very heat sensitive and breaks easily.
We recommend using a soldering iron with a temperature control function
and operating at a temperature of about 220°C to 270°C.
Even if the temperature is set that low,
the LED will be damaged if the iron is left on it for a long time,
so try to solder as quickly as possible.
Solder four LEDs at a time,
but we recommend soldering two at a time instead of four at a time
to prevent the LED temperature from rising,
as this will make it less likely to overheat.

First, check the mounting position.

Solder 1 - 6 so that the back side (under-glow) shines,
7 - 27 so that the front side (back-light) shines.
Below is the location to attach the LED (image from Corne Cherry).

![](https://user-images.githubusercontent.com/736191/46822561-c6f58d00-cdc6-11e8-90d4-de015410a7a4.png)
![](https://user-images.githubusercontent.com/736191/46822569-cc52d780-cdc6-11e8-9602-f6265a2c876d.png)

For LEDs 1 to 6,
solder the part so that the black part circled below is on the bottom
and the silk mark indicated by the arrow is on the top.
Note that the direction changes between 1 - 3 and 4 - 5.

![](https://user-images.githubusercontent.com/736191/46822428-6d8d5e00-cdc6-11e8-8858-06e8dbdb8ee8.png)

For 7 - 27,
perform soldering so that the largest pad surrounded by a circle
and the silk mark indicated by an arrow are adjacent to each other,
as shown below.

![](https://user-images.githubusercontent.com/736191/46822434-6ebe8b00-cdc6-11e8-9686-69ac88bb4389.png)

If everything was successfully soldered,
it will glow as follows.
If the LED lights only halfway,
the LEDs are connected in the order of the numbers.
Therefore, it is likely that the LED that does not emit light
or the previous LED are incorrectly soldered or damaged.

![](https://user-images.githubusercontent.com/736191/52534803-751b3e80-2d89-11e9-9588-75576942ba46.png)
![](https://user-images.githubusercontent.com/736191/52534807-7c424c80-2d89-11e9-9580-0daffc862ebb.png)
![](https://user-images.githubusercontent.com/736191/52534811-85331e00-2d89-11e9-9752-c40ffab23419.png)

### Kailh PCB Socket

![](https://user-images.githubusercontent.com/736191/52534832-be6b8e00-2d89-11e9-82e6-be53dd82bf59.png)

Apply solder to the pads on both sides on the back.
It is difficult to add it later,
so please fill it up beforehand.

![](https://user-images.githubusercontent.com/736191/52534834-c75c5f80-2d89-11e9-987e-d1ca43cf6bc3.png)

Insert the socket and melt the solder.
At this time,
hold the socket with tweezers or your fingers so that the socket sticks to the board.

![](https://user-images.githubusercontent.com/736191/52534839-d0e5c780-2d89-11e9-8579-d6967b801229.png)

The soldering is now complete.

![](https://user-images.githubusercontent.com/736191/52534855-05f21a00-2d8a-11e9-8a63-a9f8b09a730a.png)
![](https://user-images.githubusercontent.com/736191/52534859-0c809180-2d8a-11e9-959a-83c58da83844.png)

### Plate, switch

![](https://user-images.githubusercontent.com/736191/52534879-55384a80-2d8a-11e9-9648-e9e9b81625c1.png)

Use 4.5mm spacers for the top and bottom plates
and 9mm spacers for the OLED.

![](https://user-images.githubusercontent.com/736191/52534882-67b28400-2d8a-11e9-987d-00b5e14a8f2c.png)

In addition,
it is recommended to paint the side of the plate with a black marker
because it looks better.

![](https://user-images.githubusercontent.com/736191/52534914-00e19a80-2d8b-11e9-8005-7e0b157e09e4.png)

## Firmware

See below to flash the firmware to the ProMicro. \
<https://github.com/foostan/crkbd/blob/master/doc/firmware_en.md>

This is the end.

![](https://user-images.githubusercontent.com/736191/52534969-be6c8d80-2d8b-11e9-82ac-a2cd09ab96d1.png)
