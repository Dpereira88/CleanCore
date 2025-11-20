@echo off
echo ========================================
echo   CleanCore GitHub Push Script
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

REM Check if .git folder exists, if not initialize repository
if not exist ".git" (
    echo Initializing Git repository...
    git init
    if errorlevel 1 (
        echo ERROR: Failed to initialize repository
        pause
        exit /b 1
    )
    echo Git repository initialized!
    echo.
)

REM Check if remote exists, if not add it
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo Adding remote origin...
    git remote add origin https://github.com/Dpereira88/CleanCore.git
    if errorlevel 1 (
        echo ERROR: Failed to add remote
        pause
        exit /b 1
    )
    echo Remote added successfully!
    echo.
) else (
    echo Remote origin already exists
    echo.
)

REM Stage the files
echo Staging files...
git add CleanCore.py
git add README.md

REM Check if there are changes to commit
git diff --cached --quiet
if errorlevel 1 (
    echo.
    echo Files staged for commit:
    git diff --cached --name-only
    echo.
    
    REM Prompt for commit message
    set /p commit_msg="Enter commit message (or press Enter for default): "
    if "%commit_msg%"=="" set commit_msg=Update CleanCore v1.3
    
    REM Commit changes
    echo.
    echo Committing changes...
    git commit -m "%commit_msg%"
    if errorlevel 1 (
        echo ERROR: Commit failed
        pause
        exit /b 1
    )
    
    REM Ensure we're on main branch
    echo.
    echo Switching to main branch...
    git branch -M main
    
    REM Push to GitHub
    echo.
    echo Pushing to GitHub...
    git push -u origin main
    if errorlevel 1 (
        echo.
        echo WARNING: Push failed - this is normal for first push
        echo Trying force push...
        git push -u origin main --force
        if errorlevel 1 (
            echo.
            echo ERROR: Force push also failed
            echo This might be because:
            echo   1. You need to authenticate with GitHub
            echo   2. The remote URL is incorrect
            echo   3. You don't have permission to push
            echo.
            echo Please check your GitHub credentials and try again
            pause
            exit /b 1
        )
    )
    
    echo.
    echo ========================================
    echo   SUCCESS! Files pushed to GitHub
    echo ========================================
    echo.
    echo View your repository at:
    echo https://github.com/Dpereira88/CleanCore
    echo.
) else (
    echo.
    echo No changes detected in CleanCore.py or README.md
    echo Nothing to commit!
    echo.
)

pause