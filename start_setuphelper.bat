@echo off 
    if "%1" == "h" goto begin
    mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin

@set backup=.\config\backup.ini

if not exist %backup% (
    @echo config file %backup% not found, going to create it
    call pause
    cd ./bin
    call .\p2mm_cc CREATE NOT
    cd ../
)

cd ./bin
call .\p2mm_setuphelper
cd ../