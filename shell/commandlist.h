#ifndef _COMMANDLIST_H_
#define _COMMANDLIST_H_

#include<string>
#include<stdint.h>

namespace rena{

    typedef enum {
        help,
        list,
        quit,
        not_found
    }               bcmd; // basic command

    typedef struct {
        std::string command;
        bcmd        NUM;
    }               CMDLIST;

    extern CMDLIST cmdlist[];
    extern uint16_t cmdlistlength;
    

    uint16_t checkcommandlist( std::string );

}; // namespace rena

#endif