:: Download UPX and add its path to environment or add --upx-dir= PATH TO UPX
:: If you use python from anaconda, please setup a virtual environment to avoid compiling unnecessary packages
:: --add-data=icons;icons ^ --noupx ^
@echo off


pyinstaller.exe  --icon=.\icons\Widget_Box.ico ^
--exclude-module=_ssl ^
--exclude-module=ssl ^
--exclude-module=numpy ^
--exclude-module=pyqt5 ^
--exclude-module=pyqt ^
--exclude-module=matplotlib ^
--exclude-module=PyQt5.QtCore ^
--exclude-module=http ^
-w ^
-p="./" ^
hotkey_mapper.py
