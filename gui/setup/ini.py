import configparser

def readini( __filepath , __section , __key ):
    config = configparser.ConfigParser()
    config.read( __filepath )
    key_value = config.get( __section , __key )
    return key_value