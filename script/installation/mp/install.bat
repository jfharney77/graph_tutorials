@echo off
call "%~dp0\..\..\config.bat"
rem this script will generate uv .venv
call "%DEFAULT_PROJ_ROOT%\script\uv_generate_venv.bat"
rem this script will install ath
call "%DEFAULT_PROJ_ROOT%\script\installation\a\install_a.bat"
