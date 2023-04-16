FROM ubuntu:latest

RUN apt update; apt upgrade -y;

RUN apt install -y curl git build-essential clang  zip ninja-build cmake