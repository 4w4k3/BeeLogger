# Copyright 2017 Insanity Framework (IF) 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Insanity-Framework
# Licensed under the BSD-3-Clause
import os
def banner(text, char="*"):
    print(char * len(text) + "****")
    print(char + " " + text + " " + char)
    print(char * len(text) + "****")

def install_dependencies():
    """ Install the dependencies needed to run the program """
    os.system('apt-get install sudo')
    os.system('sudo dpkg --add-architecture i386')
    os.system('sudo apt-get install wget -y')
    os.system('sudo apt-get update && sudo apt-get install wine -y')
    os.system('sudo apt-get dist-upgrade -yy && apt-get upgrade -yy')
    os.system('sudo apt-get install wine32 -y')
    os.system('sudo apt-get -f install')
    os.system('sudo apt-get install wine32 -y')
    os.system('clear')
    banner("Press enter to default Winecfg to Windows 7")
    raw_input()
    os.system('winecfg')
    os.system('clear')

def download_python():
    """ Download python for some reason..? """
    banner("Downloading Python 2.7.x.msi, please wait...")
    os.system('wget https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi')
    os.system('sudo wine msiexec /i python-2.7.12.msi /L*v log.txt')

def download_python_win_exten():
    """ Download Windows extenstion for python without checking the checksum.. """
    banner("Installing pywin32-220.win32-py2.7.exe (Windows extension), please wait...")
    os.system('sudo wine pywin32-220.win32-py2.7.exe')
    os.system('sudo wine pyHook-1.5.1.win32-py2.7.exe')
    os.system('sudo wine pywin32-220.win32-py2.7.exe')
    os.system('sudo wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pip.exe install pyinstaller')
    os.system('clear')

def download_vc_for_py():
    banner("Downloading VCForPython27.msi, please wait...")
    os.system('wget https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi')
    os.system('sudo wine msiexec /i VCForPython27.msi /L*v log2.txt')
    os.system('mkdir .OK')
    os.system('sudo rm -Rf log2.txt')
    os.system('sudo rm -Rf log.txt')

def main():
    print("\n")
    banner("Installing dependencies..")
    print("\n")
    install_dependencies()
    download_python()
    print("\n")
    banner("Moving to dependent files..")
    print("\n")
    download_python_win_exten()
    download_vc_for_py()

if __name__ == '__main__':
    main()
