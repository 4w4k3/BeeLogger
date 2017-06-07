taskkill /f /im "adobeflashplayer.exe"
del /q C:\Users\Public\Libraries\adobeflashplayer.exe
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v MicrosoftUpdateXX  /f
cls
echo "[*] DONE "
pause
