sudo dpkg --add-architecture i386
sudo apt-get update --fix-missing
sudo apt-get dist-upgrade -yy && sudo apt-get upgrade -yy
sudo apt-get -f install
sudo apt-get install wine -y && sudo apt-get install wine32 -y && sudo apt-get install winbind -y
sudo winecfg
sudo wine msiexec /i python-2.7.12.msi /L*v log.txt
sudo wine pywin32-220.win32-py2.7.exe
sudo wine pyHook-1.5.1.win32-py2.7.exe
sudo wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller
