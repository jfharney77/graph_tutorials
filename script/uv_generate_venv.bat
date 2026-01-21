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

rem === Configuration section ===


rem === check to see if uv.lock exists ===
if not exist "%PROJ_ROOT%\uv.lock" (
    echo uv.lock not found in project root "%PROJ_ROOT%".
    echo Please run 'uv_generate_lock.bat' to create the lock file before generating the venv.
    exit /b 1
)

rem === check to see if pyproject.toml exists ===
if not exist "%PROJ_ROOT%\pyproject.toml" (
    echo pyproject.toml not found in project root "%PROJ_ROOT%".
    echo Please ensure pyproject.toml exists before generating the venv.
    exit /b 1
)

rem === change iunto the PROJ_ROOT directory ===
cd /d "%PROJ_ROOT%"
if errorlevel 1 (
    echo Failed to change directory to "%PROJ_ROOT%".
    exit /b 1
)

rem === Run uv sync to create/update the virtual environment ===
echo Generating virtual environment using uv...
uv sync
if errorlevel 1 (
    echo Failed to generate virtual environment using uv.
    exit /b 1
)
echo Virtual environment generated successfully.

endlocal

