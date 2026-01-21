@echo off
setlocal

rem Load shared config (path relative to this script)
call "%~dp0config.bat"
if errorlevel 1 (
    echo Failed to load config.bat
    exit /b 1
)

rem ---
rem 1) set PROJ_ROOT from first argument or default
rem ---
if "%~1"=="" (
    set "PROJ_ROOT=%DEFAULT_PROJ_ROOT%"
) else (
    set "PROJ_ROOT=%~1" 
)
echo Using project root: "%PROJ_ROOT%"

rem === Conifiguration section ===
set "VENV=%PROJ_ROOT%\pip_venv"
set "REQ=%PROJ_ROOT%\requirements_docs\requirements.txt"

rem === Ensure python is available ===
where python >nul 2>&1
if errorlevel 1 (
    echo Python is not found in PATH. Please install Python and ensure it is available in PATH.
    exit /b 1
)

rem === Create virtual environment if it doesnt exist ===
if not exist "%VENV%\Scripts\activate.bat" (
    echo Creating virtual environment at "%VENV%"
    python -m venv "%VENV%"
    if errorlevel 1 (
        echo Failed to create virtual environment.
        exit /b 1
    )
) else (
    echo Virtual environment already exists at "%VENV%"
)

rem === Activate virtual environment ===
call "%VENV%\Scripts\activate.bat"
if errorlevel 1 (
    echo Failed to activate virtual environment.
    exit /b 1
)   

rem === Verify the requirements file exists ===
if not exist "%REQ%" (
    echo Requirements file "%REQ%" does not exist.
    exit /b 1
)

rem === Upgrade pip to the latest version ===
echo Upgrading pip to the latest version...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to upgrade pip.
    exit /b 1
)   


rem === Install dependencies ===
echo Installing dependencies from "%REQ%"...
python -m pip install -r "%REQ%"
if errorlevel 1 (
    echo Failed to install dependencies.
    exit /b 1
)   
echo Dependencies installed successfully.

endlocal