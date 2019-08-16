md %cd%\outputmux\
cd /D "%~dp0"
for %%F in (%*) do call :main %%F
del %cd%\outputmux\list.txt
del %cd%\outputmux\*.ts
goto :eof

:main
setlocal
if /I "%~x1"==".mp4" set flag=1
if /I "%~x1"==".flv" set flag=1
if defined flag (
	libs\ffmpeg.exe -y -i "%~1" -vcodec copy -acodec copy -f mpegts "%~dpn1".ts
	move %cd%\*.ts %cd%\outputmux\
	(for %%a in (%cd%\outputmux\*.ts) do @echo file '%%a') > %cd%\outputmux\list.txt
	libs\ffmpeg.exe -y -safe 0 -f concat -i %cd%\outputmux\list.txt -c copy %cd%\outputmux\output.mp4
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
