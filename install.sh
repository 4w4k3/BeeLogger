sudo dpkg --add-architecture i386 && sudo apt update && sudo apt install wine32 -y
winecfg
wine msiexec /i python-2.7.12.msi /L*v log.txt
wine pywin32-220.win32-py2.7.exe
wine pyHook-1.5.1.win32-py2.7.exe
wine $HOME/.wine/drive_c/Python27/python.exe -m pip install pyinstaller
