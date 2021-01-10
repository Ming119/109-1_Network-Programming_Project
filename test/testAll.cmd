@echo off

echo '===== Running All Tests ====='
for %%i in (input/*.txt) do (
	
	"..\bin\main.py" < input/%%i
	if errorlevel 1 if not errorlevel 2 "..\bin\main.py" < input/%%i > ".\errorCatch\%%i.txt"

)

echo '===== Finish! Error outputted to "errorCatch" folder ====='
pause
