@echo off

set a=0
set b=0

setlocal EnableDelayedExpansion

for %%n in (*.flv) do (

set /A a+=1

ren "%%n" "flv!a!.flv"

)

for %%n in (*.mp4) do (

set /A b+=1

ren "%%n" "mp!b!.mp4"

)