@echo off

@rem this bat is for running PCSX2_Memcard_Manager_Shell without accessing ./bin
@rem full with dll isn't good for normal user...

@set p2mm=.\config\p2mm.ini
@set backup=.\config\backup.ini

if not exist %backup% (
    @echo backup config file not found, please do this necessary setup
    call pause
    cd ./bin
    call .\p2mm_cc CREATE NOT
    call .\p2mm_setuphelper
    cd ../
)

if not exist %p2mm% (
    @echo it seems that it's the first time the PCSX2_Memcard_Manager is being used, therefore please do necessary setup
    call pause
    cd ./bin
    call .\p2mm_setuphelper
    cd ../
)

call .\bin\p2mm_shell
@rem run PCSX2_Memcard_Manager_Shell