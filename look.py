#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 BeeLogger
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/BeeLogger
# Licensed under the BSD-3-Clause
import os
import sys
import platform

os.system('clear')
print '''\n ### PLEASE DON'T INTERRUPT THE INSTALLATION OF DEPENDENCIES ###\n'''

def banner(text, char="*"):
    print(char * len(text) + "****")
    print(char + " " + text + " " + char)
    print(char * len(text) + "****")

checker = platform.architecture()
if checker[0] == "64bit":
    if os.path.exists('.ARCHADDED'):
        print "OK"
    else:
        print "You're running 64bit System, its necessary install i386 arch."
        a = raw_input("Do you wanna continue? (y/n) [This can take a few moments]: ")
        if a.upper() == "Y":
            os.system('sudo dpkg --add-architecture i386')
            os.system('sudo apt-get dist-upgrade -yy && apt-get upgrade -yy')
            os.system('sudo apt-get -f install')
            os.system('mkdir .ARCHADDED')
        else:
            sys.exit(0)
else:
    print "Arch i386 FOUND."

banner(" ~ SEARCHING FOR WGET")
abc = os.system('which wget')
if len(str(abc)) == 1:
    print "[*] WGET FOUND"
else:
    print "[!] WGET NOT FOUND, INSTALLING IT"
    os.system("sudo apt-get install wget -y")

banner(" ~ SEARCHING FOR WINE")
abc = os.system('which wine')
if len(str(abc)) == 1:
    print "[*] WINE FOUND"
else:
    print "[!] WINE NOT FOUND, INSTALLING IT"
    os.system("sudo apt-get install wine -y")
    os.system("sudo apt-get install wine32 -y")
    os.system('sudo apt-get install winbind -y')

banner(" ~ SEARCHING FOR PYTHON2.7 ON WINE")
if os.path.exists('/root/.wine/drive_c/Python27'):
    print '/root/.wine/drive_c/Python27'
    print "[*] PYTHON 2.7 FOUND"
else:
    print "[!] PYTHON 2.7 NOT FOUND, INSTALLING IT"
    os.system('sudo wine msiexec /i python-2.7.12.msi /L*v log.txt')

banner(" ~ SEARCHING FOR PYWIN32")
if os.path.isfile("/root/.wine/drive_c/Python27/Removepywin32.exe"):
    print "/root/.wine/drive_c/Python27/Removepywin32.exe"
    print "[*] PYWIN32 FOUND"
else:
    print "[!] PYWIN32 NOT FOUND, INSTALLING IT"
    os.system('sudo wine pywin32-220.win32-py2.7.exe')

banner(" ~ SEARCHING FOR PYHOOK")
if os.path.isfile("/root/.wine/drive_c/Python27/RemovepyHook.exe"):
    print "/root/.wine/drive_c/Python27/RemovepyHook.exe"
    print "[*] PYHOOK FOUND"
else:
    print "[!] PYHOOK NOT FOUND, INSTALLING IT"
    os.system('sudo wine pyHook-1.5.1.win32-py2.7.exe')

banner(" ~ SEARCHING FOR PYINSTALLER")
if os.path.isfile("/root/.wine/drive_c/Python27/Scripts/pyinstaller.exe"):
    print "/root/.wine/drive_c/Python27/Scripts/pyinstaller.exe"
    print "[*] PYINSTALLER FOUND"
else:
    print "[!] PYINSTALLER NOR FOUND, INSTALLING IT"
    os.system('sudo wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller')
