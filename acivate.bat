@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo 仮想環境の一覧:
set count=1

for /d %%i in (C:\Users\thyt\envs\*) do (
    echo !count!. %%~nxi
    set "env!count!=%%i"
    set /a count+=1
)

echo.
set /p choice="起動したい仮想環境の番号を入力してください: "
set "selectedEnv=!env%choice%!"

if not defined selectedEnv (
    echo 無効な選択肢です。
    goto :eof
)

call :activateEnv "!selectedEnv!"
goto :eof

:activateEnv
start cmd /k "call %1\Scripts\activate.bat"
goto :eof
