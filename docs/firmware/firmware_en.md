# Firmware

## Flash the firmware for rev4
Download the firmware of VIA from below
- [crkbd_rev4_standard_via.uf2](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_standard_via.uf2)
- [crkbd_rev4_mini_via.uf2](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_mini_via.uf2)

Connect to the PC while holding down the BOOT button, or while connected to the PC, hold down the BOOT button and press the RESET button.
After that, an RPI-PR2 device will be mounted.

![btn](https://github.com/foostan/kbd_firmware/assets/736191/05fd9c4b-12c7-4a32-9606-8fea27bfe7b4)

Drop the downloaded uf2 file into the RPI-PR2 device to complete flash.

![flash](https://github.com/foostan/crkbd/assets/736191/5e5e6eab-3ad3-47f1-9871-1e2bfe554490)

Once the firmware has been written to one side, follow the same procedure for the other side.

## Flash the firmware for rev1

### Use [Remap](https://remap-keys.app/catalog/EfziB9K7ZcxLnIHXl5AQ/firmware)
The easiest and most recommended way is to go to Remap and select FLASH for crkbd:via.

![flash_by_remap](https://github.com/foostan/kbd_firmware/assets/736191/78b74abe-9853-4a5f-9577-421d39a4a380)

Once the firmware has been written to one side, follow the same procedure for the other side.

### Use [QMK Toolbox](https://github.com/qmk/qmk_toolbox)

Download the firmware of VIA from [crkbd_rev1_via.hex](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev1_via.hex)

With the keyboard connected via USB,
press the reset button **twice** or short **GND & RST** pins on ProMicro to start flashing the firmware. \
If you see the message, it's done.

![qmk_toolbox_flashed](assets/qmk_toolbox_flashed.jpg)

Once the firmware has been written to one side, follow the same procedure for the other side.

## (Optional) If you build the firmware yourself

Refer to [the QMK _getting started_ guide](https://docs.qmk.fm/#/newbs_getting_started),
and install the necessary software according to your OS
(it takes quite some time to install).

Once the environment is ready,
build the firmware for Crkbd with the following files.
https://github.com/foostan/kbd_firmware/tree/main/keyboards/crkbd/qmk/qmk_firmware

## Change your keymap

The Corne Keyboard is supported by [VIA](https://usevia.app/). \
It can be used by flashing the firmware for VIA.

### for v4

If you use Corne v4, please download json file from bellow and load at VIA
- [Corne v4](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/the-via/crkbd_rev4.json)
- [Corne v4 mini](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/the-via/crkbd_rev4_mini.json)

![load_json](https://github.com/foostan/kbd_firmware/assets/736191/67398174-0ef7-4698-9e39-6595b8320428)
![loaded_json](https://github.com/foostan/kbd_firmware/assets/736191/e3e850a8-a5c1-4116-a43d-b2b71c2f606e)
