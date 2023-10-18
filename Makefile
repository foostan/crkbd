.PHONY: pull-kbd-module
pull-kbd-module:
	git subtree pull --prefix pcb/common/kbd https://github.com/foostan/kbd.git crkbd4 --squash
