@echo off

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