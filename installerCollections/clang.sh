#!/bin/bash

prefix="$(realpath $1)"

git clone --depth=1 https://github.com/llvm/llvm-project.git
cd llvm-project
mkdir build
cd build

cmake -GNinja -DLLVM_ENABLE_PROJECTS=clang -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$prefix/llvm" ../llvm
ninja -j 2
ninja install
zip -r "$prefix/llvm.zip" "$prefix/llvm"
rm -rf "$prefix/vim"