@echo off
pyinstaller --onefile --icon="icon/icon.ico" main.pyw

mv dist/main.exe ./main.exe

rm -rfd dist/ build/ main.spec