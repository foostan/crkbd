.PHONY: git-submodule
git-submodule:
	git submodule sync --recursive
	git submodule update --init --recursive --progress
