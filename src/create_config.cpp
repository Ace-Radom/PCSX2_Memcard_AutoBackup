#include<create_config.h>

void create_backup_INI(){

#if 0    
    std::string INI;
    std::fstream wFile;
    wFile.open( "../config/backup.ini" , std::ios::out );

    INI.append( "[PCSX2]"                 ).append( "\n" )
       .append( "memcard_folder = "       ).append( "\n" )
       .append( "\n"                      )
       .append( "[PCSX2_Memcard_Manager]" ).append( "\n" )
       .append( "backup_folder = "        ).append( "\n" )
       .append( "backup_format = "        ).append( "\n" )
       .append( "\n"                      );

    //std::cout << INI;
    wFile << INI;

    wFile.close();

    return INI;
#endif

    rena::ini_file INI;
    INI["PCSX2"]["memcard_folder"];
    INI["PCSX2_Memcard_Manager"]["backup_folder"];
    INI["PCSX2_Memcard_Manager"]["backup_format"];

    INI.dump( "../config/backup.ini" );

}

void create_p2mm_INI(){
    std::string INI;
    std::fstream wFile;
    wFile.open( "../config/p2mm.ini" , std::ios::out );

    INI.append( "; =========================== ATTENTION!!! ===========================" ).append( "\n" )
       .append( ";      This ini is a configure file for the PCSX2_Memcard_Manager"      ).append( "\n" )
       .append( "; Any changes to this ini may causes unknown error to the P2MM program" ).append( "\n" )
       .append( ";            Therefore: Please don't edit this file, thanks"            ).append( "\n" )
       .append( "; ====================================================================" ).append( "\n" );

    //std::cout << INI;
    wFile << INI;

    wFile.close();

    return;
}