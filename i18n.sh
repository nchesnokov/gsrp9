#!/usr/bin/bash

pybabel extract -F babel.cfg --input-dir=gsrp5service -o gsrp5-service.pot
if [ -f gsrp5service/locale/ru_ru/LC_MESSAGE/gsrp5-service.po ]; then
 pybabel init -D gsrp5-service -d gsrp5service/locale -l ru_RU -i gsrp5-service.pot
else
  pybabel update -D gsrp5-service -d gsrp5service/locale -l ru_RU -i gsrp5-service.pot
fi
