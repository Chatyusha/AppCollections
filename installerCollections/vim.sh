#!/bin/bash

prefix="$(realpath $1)"

git clone https://github.com/vim/vim.git
cd vim/src

./configure --prefix="$prefix/vim"
make -j2
make install
zip -r "$prefix/vim.zip" "$prefix/vim"