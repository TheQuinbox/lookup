@echo off
nuitka --windows-company-name=Accessware --windows-product-name=Lookup --windows-file-version=0.11 --windows-product-version=0.11 --windows-file-description=Lookup --standalone --python-flag=no_site --windows-disable-console --remove-output lookup.pyw
pause > nul
