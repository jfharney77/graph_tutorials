@echo off
call "%~dp0..\config.bat"
set "A_DIR=%DEFAULT_PROJ_ROOT%\..\%A_NAME%"
set "PS1_FILE=%TEMP%\install_a_helper_init.ps1"

> "%PS1_FILE%" echo Set-Location '%DEFAULT_PROJ_ROOT%/../'
>> "%PS1_FILE%" echo git clone %LCMG_REPO%
>> "%PS1_FILE%" echo Set-Location '%DEFAULT_PROJ_ROOT%/../%A_NAME%'
>> "%PS1_FILE%" echo git checkout %A_BRANCH%
>> "%PS1_FILE%" echo Set-Location '%DEFAULT_PROJ_ROOT%/../%A_NAME%'
>> "%PS1_FILE%" echo .\script\uv_generate_venv.bat
>> "%PS1_FILE%" echo uv run %DEFAULT_PROJ_ROOT%/../%A_NAME%\script\run_all_a_models.bat

start powershell -NoExit -File "%PS1_FILE%"
