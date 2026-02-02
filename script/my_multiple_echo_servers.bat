@echo off
call "%~dp0config.bat"
echo Starting Echo Services on ports 6001 and 6002 in separate tabs...
wt new-tab powershell -Command "python %ECHO_SERVER_PATH% 6001" ; new-tab powershell -Command "python %ECHO_SERVER_PATH% 6002"
