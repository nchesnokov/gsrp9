#!/usr/bin/bash

pybabel extract -F babel.cfg -o gsrp5server.pot .
pybabel update -D gsrp5server -d locale -l ru_RU -i gsrp5server.pot

