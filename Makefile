# SPDX-FileCopyrightText: 2021 foostan <ks@fstn.jp>
#
# SPDX-License-Identifier: CC0-1.0

.PHONY: git-submodule
git-submodule:
	git submodule sync --recursive
	git submodule update --init --recursive --progress
