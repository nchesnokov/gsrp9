#!/usr/bin/bash
./cython.sh

#python3 ./setup.py bdist_rpm --release=3
python3 ./setup.py install --prefix=/usr
