#!/bin/bash

prefix="$(realpath $1)"
procs=$(nproc)

cd $prefix
zip -r llvm.zip llvm
rm -rf llvm