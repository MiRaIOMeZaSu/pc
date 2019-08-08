@echo off
REM 功能：一键无损重新封装为 mp4
REM 备注：暂时只支持FLV和MKV格式

REM echo %~n1%~x1
REM echo %~1
REM echo %~dp0
REM echo %~dpn1
REM ping -n 10 127.0.0.1 > nul 可当作 wait


title 一键无损重新封装为 mp4

cd /D "%~dp0"
for %%F in (%*) do call :main %%F
goto :eof

:main
setlocal
if /I "%~x1"==".flv" set flag=1
if /I "%~x1"==".mkv" set flag=1
if defined flag (
	libs\ffmpeg.exe -i "%~1" -vcodec copy -acodec copy "%~dpn1".mp4
	goto :eof
)
if not defined flag (
	echo ===
	echo === 文件名: %~n1%~x1
	echo === 错误原因：格式不支持
	echo ===
	pause
)
endlocal
goto :eof