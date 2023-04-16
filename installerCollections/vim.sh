#!/bin/bash

prefix="$(realpath $1)"
procs=$2

git clone https://github.com/vim/vim.git
cd vim/src

./configure --prefix="$prefix/vim"
make -j $procs
make install
zip -r "$prefix/vim.zip" "$prefix/vim"