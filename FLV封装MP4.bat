@echo off
REM ���ܣ�һ���������·�װΪ mp4
REM ��ע����ʱֻ֧��FLV��MKV��ʽ

REM echo %~n1%~x1
REM echo %~1
REM echo %~dp0
REM echo %~dpn1
REM ping -n 10 127.0.0.1 > nul �ɵ��� wait


title һ���������·�װΪ mp4

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
	echo === �ļ���: %~n1%~x1
	echo === ����ԭ�򣺸�ʽ��֧��
	echo ===
	pause
)
endlocal
goto :eof