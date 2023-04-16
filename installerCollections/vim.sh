#!/bin/bash

prefix="$(realpath $1)"
procs=$(nproc)

git clone https://github.com/vim/vim.git
cd vim/src

./configure --prefix="$prefix/vim"
make -j $procs
make install
cd $prefix
zip -r vim.zip vim
rm -rf vim