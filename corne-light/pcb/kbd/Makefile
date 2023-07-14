.PHONY: tools
tools:
	if [ -d kicad-library-utils ]; then rm -rf kicad-library-utils; fi
	git clone --depth 1 https://github.com/KiCad/kicad-library-utils kicad-library-utils

.PHONY: kicad-symbols-comparelibs
kicad-symbols-comparelibs:
	if [ -d old ]; then rm -rf old; fi
	git clone --depth 1 https://github.com/foostan/kbd old
	cd kicad-library-utils/schlib; \
          ./comparelibs.py --new ../../kicad-symbols/*.lib --old ../../kbd-old/kicad-symbols/*.lib --check -v

.PHONY: kicad-symbols-check-lib-table
kicad-symbols-check-lib-table:
	cd kicad-library-utils; \
          ./check_lib_table.py ../kicad-symbols/*.lib --table ../kicad-symbols/sym-lib-table

.PHONY: kicad-footprints-check-all
kicad-footprints-check-all:
	cd kicad-library-utils/pcb; \
	  ./check_kicad_mod.py ../../kicad-footprints/kbd.pretty/*.kicad_mod -vv

.PHONY: kicad-footprints-check-lib-table
kicad-footprints-check-lib-table:
	cd kicad-library-utils; \
	  ./check_lib_table.py ../kicad-footprints/*.pretty --table ../kicad-footprints/fp-lib-table
