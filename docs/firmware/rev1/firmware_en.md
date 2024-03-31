# Firmware
This is the Corne v1-v3(rev1) firmware guide。

## Flash the firmware

### Use [Remap](https://remap-keys.app/catalog/EfziB9K7ZcxLnIHXl5AQ/firmware)
The easiest and most recommended way is to go to Remap and select FLASH for crkbd:via.

![flash_by_remap](https://github.com/foostan/kbd_firmware/assets/736191/78b74abe-9853-4a5f-9577-421d39a4a380)

Once the firmware has been written to one side, follow the same procedure for the other side.

### Use [QMK Toolbox](https://github.com/qmk/qmk_toolbox)

Download the firmware of VIA from [crkbd_rev1_via.hex](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev1_via.hex)

With the keyboard connected via USB,
press the reset button **twice** or short **GND & RST** pins on ProMicro to start flashing the firmware. \
If you see the message, it's done.

![qmk_toolbox_flashed](https://github.com/foostan/crkbd/assets/736191/1a3fdd38-adcd-4c45-82f3-0daf4ef96f4f)

Once the firmware has been written to one side, follow the same procedure for the other side.

## (Optional) If you build the firmware yourself
Please refer to https://github.com/foostan/kbd_firmware.

## Change your keymap

[VIA](https://usevia.app/) can be used by flashing the firmware for VIA. 

![via_begin](https://github.com/foostan/crkbd/assets/736191/ffffab0f-ee66-462b-8266-90214c3551ac)