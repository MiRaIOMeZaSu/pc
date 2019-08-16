@echo off

md %cd%\outputmp4\
cd /D "%~dp0"
for %%F in (%*) do call :main %%F
goto :eof

:main
setlocal
if /I "%~x1"==".flv" set flag=1
if defined flag (
	libs\ffmpeg.exe -i "%~1" -vcodec copy -acodec copy "%~dpn1".mp4
	move %cd%\*.mp4 %cd%\outputmp4\
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
