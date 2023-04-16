#!/bin/bash

prefix="$(realpath $1)"
procs=$(nproc)

git clone --depth=1 https://github.com/llvm/llvm-project.git
cd llvm-project
mkdir build
cd build

cmake -GNinja -DLLVM_ENABLE_PROJECTS=clang -DLLVM_ENABLE_RUNTIMES="libc;libcxx" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$prefix/llvm" ../llvm
ninja -j $procs
ninja install
cd $prefix
zip -r llvm.zip llvm
rm -rf llvm