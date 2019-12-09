#!/usr/bin/bash

FILES=`python3 build.py gsrp5server server.py client.py listener.py __init__.py`

for FILE in $FILES
  do
    if [ $FILE.py -nt $FILE.c ]
      then
        echo Cython $FILE.py
        cython -t -3 $FILE.py
    fi
  done
