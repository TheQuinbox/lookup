@echo off
xcopy /Q /E docs\documentation.html lookup.dist /Y
xcopy /Q /E lib lookup.dist /Y
pause > nul
