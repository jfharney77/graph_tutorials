@echo off
echo Stopping all echo server processes...
rem powershell -Command "Get-CimInstance Win32_Process | Where-Object {$_.CommandLine -like '*echo_server.py*' -or $_.CommandLine -like '*echo_server2.py*'} | ForEach-Object {Stop-Process -Id $_.ProcessId -Force}"
powershell -Command "Get-CimInstance Win32_Process | Where-Object {$_.CommandLine -like '*echo_server.py*'} | ForEach-Object {Stop-Process -Id $_.ProcessId -Force}"
powershell -Command "Get-CimInstance Win32_Process | Where-Object {$_.CommandLine -like '*echo_server2.py*'} | ForEach-Object {Stop-Process -Id $_.ProcessId -Force}"

echo Echo servers stopped.
