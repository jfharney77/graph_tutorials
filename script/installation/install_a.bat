@echo off
call "%~dp0..\config.bat"
set "A_DIR=%DEFAULT_PROJ_ROOT%\..\%A_NAME%"
echo installing a... "%A_DIR%"
if exist "%A_DIR%" (
	call "%~dp0install_a_helper.bat"
) else (
	echo it does not exist
	echo %A_DIR%
	call "%~dp0install_a_helper_init.bat"
)
