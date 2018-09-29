# By Nerex
# GitHub: NerexNX

import urllib.request
from urllib.request import urlopen, Request
import itertools
from itertools import cycle
import base64

LEVEL_NOT_FOUND_ERROR = "NO_LEVELS_FOUND"
USER_NOT_FOUND_ERROR = "USER_NOT_FOUND"
SONG_NOT_FOUND_ERROR = "SONG_NOT_FOUND"

def StructParams(params):
    FinalParams = ""
    for value in params:
        if value == "secret":
            FinalParams += value + "=" + params[value]
        else:
            FinalParams += value + "=" + params[value] + "&"
    FinalParams = FinalParams.encode()
    return FinalParams
    
def SendHTTPRequest(php, params):
    BaseURL = "http://www.boomlings.com/database/"
    URL = BaseURL + php + ".php"

    URLParameters = StructParams(params)
    
    data = urlopen(URL, URLParameters).read().decode()
    return data

def GetDifficulty(List):
    leveldifficulty = None
    
    if List[11] == "50":
        if List[21] == "1":
            leveldifficulty = "Extreme Demon"
        elif List[25] == "1":
            leveldifficulty = "Auto"
        else:
            leveldifficulty = "Insane"    
    elif List[11] == "40":
        if List[27] == "10":
            leveldifficulty = "Insane Demon"
        else:
            leveldifficulty = "Harder"        
    elif List[11] == "30":
        if List[27] == "10":
            leveldifficulty = "Hard Demon"
        else:
            leveldifficulty = "Hard"
    elif List[11] == "20":
            if List[27] == "10":
                leveldifficulty = "Medium Demon"
            else:
                leveldifficulty = "Normal"
    elif List[11] == "10":
            if List[27] == "10":
                leveldifficulty = "Easy Demon"
            else:
                leveldifficulty = "Easy"
    elif List[11] == "0":
        leveldifficulty = "N/A"
        
    return leveldifficulty

def GetLength(lengthint):
    length = "(?)"
    
    if lengthint == "0":
        length = "Tiny"
    elif lengthint == "1":
        length = "Short"
    elif lengthint == "2":
        length = "Medium"
    elif lengthint == "3":
        length = "Long"
    elif lengthint == "4":
        length = "XL"

    return length

def StructureUser(parser):

    try:
        ## Create a dictionnary
        StructuredUser = {
            "username": parser[1],
            "stars": parser[13],
            "usercoins": parser[7],
            "demons": parser[17],
            "diamonds": parser[15],
            "cp": parser[19],
            "youtube": parser[27],
            "twitter": "@"+parser[53],
            "twitch": parser[55],
            "accountid": parser[3],
            "userid": parser[49]
       }
    except:
        raise Exception

    return StructuredUser
