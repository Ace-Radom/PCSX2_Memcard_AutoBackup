#include<create_config.h>

std::string create_backup_INI(){
    std::string INI;
    std::fstream wFile;
    wFile.open( "../config/backup.ini" , std::ios::out );

    INI.append( "[PCSX2]" )                  .append( "\n" )
       .append( "memcard_folder = " )        .append( "\n" )
       .append( "\n" )
       .append( "[PCSX2_Memcard_Manager]" )  .append( "\n" )
       .append( "backup_folder = " )         .append( "\n" )
       .append( "backup_format = " )         .append( "\n" )
       .append( "\n" );

    //std::cout << INI;
    wFile << INI;

    return INI;
}

std::string create_p2mm_INI(){
    //std::cout << "progressing" << std::endl;
    return "";
}