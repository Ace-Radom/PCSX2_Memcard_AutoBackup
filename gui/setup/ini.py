import configparser


def rINI( __filepath , __section , __key ):
    config = configparser.ConfigParser()
    config.read( __filepath , encoding = "utf-8" )
    key_value = config.get( __section , __key )
    return key_value

def wINI( __filepath , __section , __key , __value ):
    config = configparser.ConfigParser()
    config.read( __filepath , encoding = "utf-8" )
    config.set( __section , __key , __value )
    with open( __filepath , 'w' , encoding = "utf-8" ) as wFile:
        config.write( wFile )
