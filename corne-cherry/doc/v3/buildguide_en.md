# Build Guide

This is the build guide for Corne Cherry v3.
[Click here for Corne Cherry v2](
https://github.com/foostan/crkbd/blob/master/corne-cherry/doc/v2/buildguide_en.md).

## Parts

### Required

| Name | Number | Remarks |
|:-|:-|:-|
| PCB | 1 set | |
| Top plate | 2 sheets | |
| Bottom plate | 2 sheets | |
| OLED protective plate | 2 sheets | |
| ProMicro | 2 sheets | |
| TRRS jack | 2 | |
| Tact switch | 2 | |
| Diodes | 42 | Only SMD parts are supported |
| PCB sockets | 42 | Compatible with Kailh and Gateron |
| Key switches | 42 | Only compatible with CherryMX |
| Keycaps | 42 pcs | 1u 40 pcs, 1.5u 2 pcs |
| Spacer M2 7.5mm | 10 pieces | |
| Spacer M2 9mm | 4 pieces | |
| Screw M2 4mm | 28 screws | |
| Cushion rubber | 8 pieces | |
| TRRS (4 poles) cable | 1 | TRS (3 poles) cable is also acceptable |
| Micro USB cable | 1 | |

### Options

| Name | Number | Remarks |
|:-|:-|:-|
| OLED module | 2 sheets | |
| Pin header for OLED module 4 series 1.5mm | 2 | |
| 4 pin sockets for OLED module 2.5mm | 2 | |
| SK6812MINI-E | 42 pieces | LEDs for Back light |
| WS2812B | 12 | LEDs for Undergrow |

## Advance preparation

If you build the firmware yourself,
it takes time to prepare the environment,
so it is recommended to start first. \
See <https://github.com/foostan/crkbd/blob/master/doc/firmware_en.md>
for more information.

## Verification

The PCB for Corne Cherry v3 is as follows.
Make sure it is the same as your PCB.

![confirm_front](assets/confirm_front.jpg)

![confirm_back](assets/confirm_back.jpg)

The PCB comes with a frame for manufacturing reasons.
You can fold it by hand to remove it, but if it is difficult,
make a cut in the joint \* with a cutter etc. to make it easier to remove.
In addition, the joint can be cleaned with a file.

\* *Joint part: There are a total of 8 parts,
which are marked in red in the image below.*

![confirm_remove_frame](assets/confirm_remove_frame.jpg)

## Assembly

### Diode

Solder diodes for SMD components.
Since SMD parts are very small,
it is convenient to have tweezers and counter-acting tweezers.

**The diode has a fixed mounting direction**,
and solder it so that the "|" mark on the part faces the "|" on the diode mark "|◁".
In addition, Corne's PCB has all the same diode mounting orientations.

![build_diode](assets/build_diode.jpg)

<details>
<summary>TIPS: Tips for installing SMD parts</summary>

The trick is to attach the SMD parts, but first, as a spare solder,
put the solder on only one side of the pad.

![tips_building_smd_01](https://user-images.githubusercontent.com/736191/54487435-79330280-48d9-11e9-9138-525d8ee68144.jpg)

Next, solder one leg of the diode so that the spare solder melts.
At this time, it is recommended to use reverse-action tweezers,
because you can hold the chip parts firmly without exerting force
and you can concentrate on alignment and soldering.
Also, if the soldering iron is too hot or the solder is touched too much,
the flux contained in the solder may evaporate and form a clean pile of solder,
but it can be repaired later,
so at this point you should only be aware of attaching parts.
It's okay.

![tips_building_smd_02](https://user-images.githubusercontent.com/736191/54487436-79330280-48d9-11e9-856e-f3f5b9f58414.jpg)

It is okay if the diode does not float when viewed from the side
when one foot is attached.
If it floats, press the diode with tweezers or your fingers
and reheat the soldered part with a soldering iron to clean it.

![tips_building_smd_03](https://user-images.githubusercontent.com/736191/54487437-79330280-48d9-11e9-996d-a578e767c12c.jpg)

Then solder the other one. Be careful not to apply too much,
as a small amount of solder is sufficient.
If you apply too much, you can remove it with a blotting wire
or by scooping it with a soldering iron.

If the amount of solder on the preliminary solder side is small,
additional soldering is performed, and if it is a mountain,
apply flux from above and heat it to clean it.

![tips_building_smd_04](https://user-images.githubusercontent.com/736191/54487438-79cb9900-48d9-11e9-9280-dc72a2087307.jpg)

</details>

The diode is completed by soldering 42 pieces in total on the left and right.

![build_diode_overview](assets/build_diode_overview.jpg)

### LED (optional)

Solder the SK6812MINI-E and WS2812B.

First, check the state after installation.

![build_led_front_overview](assets/build_led_front_overview.jpg)

All soldering is done from the back side, but the SK6812MINI-E is for Backlight
(the front side is shining) and the WS2812B is for Undergrow (the back side is shining).
![build_led_back_overview](assets/build_led_back_overview.jpg)

#### WS2812B (Undergrow)

First, solder the WS2812B.

Solder with the corners of the recesses on the WS2812B
and the corner marks on the PCB aligned as shown below.
**TIPS: As I introduced in Tips for Installing SMD Parts**,
I think that you can attach it well with spare solder.

In addition, his PCB of Corne has the same mounting orientation of his WS2812B.

![build_led_undergrow](assets/build_led_undergrow.jpg)

He soldered a total of 8 pieces on the left and right, and he completed the WS2812B.

![build_led_undergrow_overview](assets/build_led_undergrow_overview.jpg)

#### SK6812MINI-E (Backlight)

Then solder the SK6812MINI-E.

Solder the SK6812MINI-E with the missing corners aligned with the PCB corners
as shown below.
**TIPS: As I introduced in Tips for Installing SMD Parts**,
I think that you can attach it well with spare solder.
It is harder to break than the SK6812MINI,
but it may be damaged if it is directly exposed to the heat of a soldering iron.
If the temperature is about 320°C
with a soldering iron with a temperature control function,
it seems that there is no problem even if four legs are soldered continuously.

All Corne PCBs have the same mounting orientation for the SK6812MINI-E.

![build_led_backlight](assets/build_led_backlight.jpg)

SK6812MINI-E is completed by soldering a total of 42 pieces on the left and right.

![build_led_back_overview](assets/build_led_back_overview.jpg)

### TRRS jack, reset switch, pin socket for OLED

Solder the TRRS jack, reset switch (tact switch),
and OLED pin socket as shown in the picture below.

![build_trrs_reset_oled](assets/build_trrs_reset_oled.jpg)

Since it is a part that easily slips off,
you can solder it while holding the part by hand,
or fix it with masking tape and then solder it.

### ProMicro

Solder ProMicro in the following orientation

![build_promicro](assets/build_promicro.jpg)

If you use Conthru, you do not need to solder the back side.
Please refer to [Helix Build Guide](
https://github.com/MakotoKurauchi/helix/blob/master/Doc/buildguide_en.md#pro-micro)
for details on how to use Consul.

![build_promicro_conthrough](assets/build_promicro_conthrough.jpg)

### OLED module

Insert the pin header into the pin socket for OLED first,
and then solder the pin header and OLED module.
At this time, the OLED module is easy to float,
so be careful not to float it while pressing it with your finger.

![build_oled](assets/build_oled.jpg)

## Firmware

Write the firmware to ProMicro by referring to the following. \
<https://github.com/foostan/crkbd/blob/master/doc/firmware_en.md>

### Operation check

We recommend that you check the operation when the ProMicro and OLED module are attached.
If you do it at the very end, it will be difficult to isolate the problem.

To check the operation, connect the left hand side to the PC with MicroUSB,
and connect the left hand side and the right hand side with the TRRS cable.
Since there may be defects such as jacks,
be sure to connect the left and right instead of one by one before checking the operation.
If it is done correctly so far,
if you short the pad to attach the PCB socket with tweezers etc.,
the key pressed on the OLED module will be displayed.

### PCB socket

Solder the PCB socket according to the mark as shown below.
All the PCB sockets are listed below,
but I'm not really into it,
so attach them one by one.
**TIPS: As I introduced in Tips for Installing SMD Parts**,
I think that you can attach it well with spare solder.

![build_socket](assets/build_socket.jpg)

The PCB socket is completed by soldering a total of 42 left and right.

![build_socket_overview](assets/build_socket_overview.jpg)

### OLED protective plate

Install the OLED protective plate with M2 9mm spacers and M2 screws.

![build_oled_plate_front](assets/build_oled_plate_front.jpg)
![build_oled_plate_back](assets/build_oled_plate_back.jpg)

### Plates, switches

After attaching the key switch to the top plate,
fit the key switch into the socket.
If you attach all the key switches to the top plate first,
it will be more difficult to fit them in the socket,
so it is easier to attach only the end key switches first.
![build_top_plate_switches](assets/build_top_plate_switches.jpg)

Install the M2 7.5mm spacer and M2 screws on the top plate.

![build_screws_spacers_front](assets/build_screws_spacers_front.jpg)

It is easy to screw the spacer after inserting it into the hole from the back side.

![build_screws_spacers_back](assets/build_screws_spacers_back.jpg)

Attach the bottom plate with M2 screws.

![build_bottom_plate](assets/build_bottom_plate.jpg)

Install the cushion rubber in the following positions.

![build_cushion_rubbers](assets/build_cushion_rubbers.jpg)

That's it.

![build_finish](assets/build_finish.jpg)
