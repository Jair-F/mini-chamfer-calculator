#!/bin/bash

pyinstaller --onefile --icon="icon/icon.ico" main.pyw

mv dist/main ./main

rm -rfd dist/ build/ main.spec