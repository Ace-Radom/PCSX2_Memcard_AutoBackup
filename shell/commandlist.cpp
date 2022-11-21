#include"commandlist.h"

rena::CMDLIST rena::cmdlist[] = {
    { "help" , rena::bcmd::help },
    { "list" , rena::bcmd::list },
    { "quit" , rena::bcmd::quit }
};

uint16_t rena::cmdlistlength = sizeof( cmdlist ) / sizeof( rena::CMDLIST );

uint16_t rena::checkcommandlist( std::string __cmd ){
    for ( int i = 0 ; i < cmdlistlength ; i++ )
    {
        if ( __cmd == cmdlist[i].command )
        {
            return cmdlist[i].NUM;
        }
    }
    return bcmd::not_found;
}