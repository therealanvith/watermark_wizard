@echo off
title One-Click Python + pip + Pillow Installer
echo =====================================================
echo     Python + pip + Pillow Full Auto Installer
echo =====================================================

:: Step 1 — Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [INFO] Python not found. Downloading latest version...
    set PYTHON_INSTALLER=%temp%\python_installer.exe

    :: Download the latest Python 3 Windows installer (64-bit)
    curl -L -o "%PYTHON_INSTALLER%" https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe

    if not exist "%PYTHON_INSTALLER%" (
        echo [ERROR] Failed to download Python installer.
        pause
        exit /b
    )

    echo.
    echo [INFO] Installing Python silently with Add to PATH...
    "%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1 Include_test=0

    echo.
    echo [INFO] Python installation completed. Cleaning up...
    del "%PYTHON_INSTALLER%" >nul 2>&1
) else (
    echo [INFO] Python already installed.
)

:: Step 2 — Ensure pip exists
echo.
echo [INFO] Checking for pip...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Installing pip...
    curl -s https://bootstrap.pypa.io/get-pip.py -o "%temp%\get-pip.py"
    python "%temp%\get-pip.py"
    del "%temp%\get-pip.py" >nul 2>&1
) else (
    echo [INFO] pip already installed.
)

:: Step 3 — Upgrade pip (for safety)
echo.
echo [INFO] Upgrading pip...
python -m pip install --upgrade pip

:: Step 4 — Install Pillow
echo.
echo [INFO] Installing Pillow (image library)...
python -m pip install pillow

if %errorlevel% neq 0 (
    echo [ERROR] Pillow installation failed.
    pause
    exit /b
)

:: Step 5 — Verify installation
echo.
echo [INFO] Verifying Pillow...
python -c "import PIL; print('[SUCCESS] Pillow installed successfully! Version:', PIL.__version__)" || echo [ERROR] Pillow not found.

echo.
echo =====================================================
echo   ✅ All Done! Python, pip, and Pillow are installed.
echo =====================================================

pause

mkdir input_images\dopy_w__atmos_w input_images\dopy_w__atmos_b input_images\dopy_b__atmos_w input_images\dopy_b__atmos_b output_images

exit
