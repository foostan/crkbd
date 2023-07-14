.PHONY: pull-kbd-module
pull-kbd-module:
	# git subtree pull --prefix corne-cherry/pcb/kbd https://github.com/foostan/kbd.git main --squash
	# git subtree pull --prefix corne-chocolate/pcb/kbd https://github.com/foostan/kbd.git main --squash
	# git subtree pull --prefix corne-light/pcb/kbd https://github.com/foostan/kbd.git main --squash
	# git subtree pull --prefix corne-classic/pcb/kbd https://github.com/foostan/kbd.git main --squash
	git subtree pull --prefix pcb/kbd https://github.com/foostan/kbd.git crkbd4 --squash
