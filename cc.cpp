// create_config

#include"create_config.h"
#include<string.h>

#define BACKUP_CONFIG 1
#define P2MM_CONFIG   2

int main( int argc , char** argv ){

    if ( strcmp( argv[BACKUP_CONFIG] , "CREATE" ) == 0 )
    {
        create_backup_INI();
    }

    if ( strcmp( argv[P2MM_CONFIG] , "CREATE" ) == 0 )
    {
        create_p2mm_INI();
    }

    return 0;

}