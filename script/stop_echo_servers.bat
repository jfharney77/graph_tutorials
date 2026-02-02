@echo off
echo Stopping all echo server processes...
powershell -Command "Get-CimInstance Win32_Process | Where-Object {$_.CommandLine -like '*echo_server.py*'} | ForEach-Object {Stop-Process -Id $_.ProcessId -Force}"
echo Echo servers stopped.
