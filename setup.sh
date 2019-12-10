#!/usr/bin/bash
./cython.sh
#python3 ./setup.py bdist_rpm
python3 ./setup.py install --prefix=/usr
