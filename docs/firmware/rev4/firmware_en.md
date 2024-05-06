# Firmware
This is the Corne v4(rev4) firmware guide.

## Flash the firmware
Please check the pcb version v4.0.0 or v4.1.0 first.\
After that, download the firmware of VIA/Vial from below.

standard (3x6) v4.0.0

- [crkbd_rev4_0_standard_via.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_0_standard_via.uf2)
- [crkbd_rev4_0_standard_vial.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/vial-kb/vial-qmk/.build/crkbd_rev4_0_standard_vial.uf2)

mini (3x5) v4.0.0

- [crkbd_rev4_0_mini_via.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_0_mini_via.uf2)
- [crkbd_rev4_0_mini_vial_mini.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/vial-kb/vial-qmk/.build/crkbd_rev4_0_mini_vial_mini.uf2)

standard (3x6) v4.1.0

- [crkbd_rev4_1_standard_via.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_1_standard_via.uf2)
- [crkbd_rev4_1_standard_vial.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/vial-kb/vial-qmk/.build/crkbd_rev4_1_standard_vial.uf2)

mini (3x5) v4.1.0

- [crkbd_rev4_1_mini_via.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/qmk/qmk_firmware/.build/crkbd_rev4_1_mini_via.uf2)
- [crkbd_rev4_1_mini_vial_mini.uf2](https://github.com/foostan/kbd_firmware/raw/main/keyboards/crkbd/vial-kb/vial-qmk/.build/crkbd_rev4_1_mini_vial_mini.uf2)

Connect to the PC while holding down the BOOT button, or while connected to the PC, hold down the BOOT button and press the RESET button.
After that, an RPI-PR2 device will be mounted.

![btn](https://github.com/foostan/kbd_firmware/assets/736191/05fd9c4b-12c7-4a32-9606-8fea27bfe7b4)

Drop the downloaded uf2 file into the RPI-PR2 device to complete flash.

![flash](https://github.com/foostan/crkbd/assets/736191/5e5e6eab-3ad3-47f1-9871-1e2bfe554490)

Once the firmware has been written to one side, follow the same procedure for the other side.

## (Optional) If you build the firmware yourself
Please refer to https://github.com/foostan/kbd_firmware.

## Change your keymap

### VIA

[VIA](https://usevia.app/) can be used by flashing the firmware for VIA. \
If you use Corne v4, please download json file from bellow and load at VIA(You need to enable Design tab at the config page)

- [Corne v4](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/the-via/crkbd_rev4.json)
- [Corne v4 mini](https://github.com/foostan/kbd_firmware/blob/main/keyboards/crkbd/the-via/crkbd_rev4_mini.json)

![enable_design_tab](https://github.com/foostan/crkbd/assets/736191/fa909532-4151-4190-8820-2ebb7d542517)
![load_json](https://github.com/foostan/kbd_firmware/assets/736191/67398174-0ef7-4698-9e39-6595b8320428)
![loaded_json](https://github.com/foostan/kbd_firmware/assets/736191/e3e850a8-a5c1-4116-a43d-b2b71c2f606e)

### Vial

[Vial](https://vial.rocks/) can be used by flashing the firmware for Vial.

![Vial](https://github.com/foostan/crkbd/assets/736191/721bd9a3-e832-4322-8cba-1a18622805de)
