@echo off
call "%~dp0..\config.bat"
set "A_DIR=%DEFAULT_PROJ_ROOT%\..\%A_NAME%"
set "PS1_FILE=%TEMP%\install_a_helper.ps1"

> "%PS1_FILE%" echo Set-Location '%A_DIR%'
>> "%PS1_FILE%" echo git remote update
>> "%PS1_FILE%" echo git pull origin %A_BRANCH%
>> "%PS1_FILE%" echo .\script\uv_generate_venv.bat
>> "%PS1_FILE%" echo uv run .\script\run_all_a_models.bat

start powershell -NoExit -File "%PS1_FILE%"
