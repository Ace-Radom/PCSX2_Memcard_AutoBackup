#include<iostream>
#include<string>

#include"../include/formathelp.h"
#include"commandlist.h"

#define FOREVER true

int main(){
    std::string readin;

    std::cout << "============================================================================" << "\n"
              << "===                  PCSX2 Memcard Manager Shell v2.0.0                  ===" << "\n"
              << "===  Project Source: https://github.com/Ace-Radom/PCSX2_Memcard_Manager  ===" << "\n"
              << "===        For more infos please visit this project's Github site        ===" << "\n"
              << "===             Still in developing, thanks for your support             ===" << "\n"
              << "============================================================================" << "\n"
              << "\n";
    // print shell begin

#pragma region shell

    while ( FOREVER )
    {
        std::cout << "PCSX2 Memcard Manager> ";
        // beginning of each line

        std::getline( std::cin , readin );
        rena::allcharlower( readin );
        // readin command and low all characters

//      std::cout << readin << std::endl; // debug
//      debug line: check the readin command after function allcharlower        

//      std::cout << rena::checkcommandlist( readin ) << std::endl; // debug
//      debug line: check function checkcommandlist

        switch ( rena::checkcommandlist( readin ) ){
            case rena::bcmd::quit: // quit shell
                return 0;
                break;
        }
    }

#pragma endregion shell
    
    return 0;

}

#undef FOREVER