@echo off
echo Checking for Python...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Checking for pip...
pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo pip is not installed. Please install pip.
    pause
    exit /b 1
)

echo Installing required packages...
pip install -r requirements.txt
if %ERRORLEVEL% EQU 0 (
    echo Installation successful! Starting the application...
    python main.py
) else (
    echo Installation failed. Please check your Python and pip installation.
    pause
)