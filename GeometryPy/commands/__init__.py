# By Nerex
# GitHub: NerexGD

import GeometryPy.utils as utils
import base64

##################################################
##                                              ##
##  GET USERS INFORMATIONS                      ##
##  PARAMS: ACCOUNTID or USERNAME               ##
##                                              ##

def GetUserInfo(str(User)):
    AccountID = User
    
    if User == "":
        return
    elif not User.isdigit():

        ## Get AccountID using Username
        URLParameters = {
            "gameVersion": "21",
            "binaryVersion": "35",
            "gdw": "0",
            "str": User,
            "secret": "Wmfd2893gb7"
        }        
        Response = utils.SendHTTPRequest("getGJUsers20", URLParameters)
        
        if Response != "-1":
            AccountID = Response.split(":")[21]
        else:
            return -1
        
    ## Search Player
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "targetAccountID": AccountID,
        "secret": "Wmfd2893gb7"
    }
    Response = utils.SendHTTPRequest("getGJUserInfo20", URLParameters)
    
    if Response == "-1":          
        return -1
    
    DataParser = Response.split(":")
    UserInfos = utils.StructureUser(DataParser)
        
    return UserInfos

##################################################
##                                              ##
##  GET LEVEL INFORMATIONS USING HTTP REQUESTS  ##
##  PARAMS: LEVELNAME and AUTHOR (optional)     ##
##                                              ##

def GetLevelInfo(LevelName, creator=None):
    if creator == "" or creator == None:
        result = GetLevelInfoByName(LevelName)
        return result
    else:
        result = GetLevelInfoByAuthor(creator)
        return result
    
##################################################        
##                                              ##
##   GET LEVEL USING LEVELNAME + CREATOR NAME   ##
##                                              ##
        
def GetLevelInfoByAuthor(LevelName, str(Creator)):
   
    #Get the accountID of the researched creator
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "str": Creator,
        "total": "0",
        "page": "0",
        "secret": "Wmfd2893gb7"}
    
    Response = utils.SendHTTPRequest("getGJUsers20", URLParameters)
    
    if Response == "-1":        
        return -1

    AccountID = str(Response.split(":")[3])
    
    #Use the accountID of the author to fetch his levels
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "str": AccountID,
        "len": "-",
        "type": "5",
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": "0",
        "epic": "0",
        "secret": "Wmfd2893gb7"
    }
    Response = utils.SendHTTPRequest("getGJLevels21", URLParameters)

    if Response == "-1":           
        return -1
    
    LevelParser = recdata.split("|")
    LevelIndex = 0
    AuthorIndex = 0
    
    #Look for each levels in creator account to see if level name correspond to the researched one
    for i in range(len(LevelParser)):
        ThisLevel = LevelParser[i].split(":")
        
        if ThisLevel[3].lower() == levelName.lower():
            LevelIndex = i
            break
        elif i == len(LevelParser) - 1:
            LevelIndex = -1
            break

    #Check if level found
    if levelIndex == -1:
        return utils.LEVEL_NOT_FOUND_ERROR
    else:        
        try:
            LevelData = LevelParser[levelIndex].split(":")
            AuthorsData = Response.split("#")[1].split("|")
            
            for i in range(len(AuthorsData)):
                try:
                    if AuthorsData[i].split(":")[0] == LevelData[7]:
                        AuthorIndex = i
                        break
                except:
                    pass

            if LevelData[39] == "0":
                LevelData[39] = "true"
                
            LevelInfos = {
                "name": LevelData[3],
                "author": {
                    "name": AuthorsData[authorIndex].split(":")[1],
                    "accountid": AuthorsData[authorIndex].split(":")[0],
                    "userid": AuthorsData[authorIndex].split(":")[2]
                    },
                "id": LevelData[1],
                "downloads": LevelData[13],
                "likes": LevelData[19],
                "description": LevelData.b64decode(str(LevelData[35])).decode(),
                "original": LevelData[39],
                "difficulty": utils.GetDifficulty(LevelData),
                "length": utils.GetLength(LevelData[37])}
        except:
            return -1
        
        return LevelInfos
    
##                                              ##
##   GET LEVEL INFORMATIONS USING LEVEL NAME    ##
##                                              ##
    
def GetLevelInfoByName(str(LevelName)):   
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "str": LevelName,
        "len": "-",
        "type": "0",
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": "0",
        "epic": "0",
        "secret": "Wmfd2893gb7"

    }
    Response = utils.SendHTTPRequest("getGJLevels21", URLParameters)

    if Response == "-1":        
        return -1
    
    LevelParser = Response.split("|")
    AuthorIndex = 0
    
    try:
        LevelData = LevelParser[0].split(":")
        AuthorsData = Response.split("#")[1].split("|")

        #Find level author informations
        for i in range(len(AuthorsData)):
            try:
                if AuthorsData[i].split(":")[0] == LevelData[7]:
                    AuthorIndex = i
                    break
            except:
                pass

        if LevelData[39] == "0":
            LevelData[39] = "true"
            
        LevelInfos = {
            "name": LevelData[3],
            "author": {
                "name": AuthorsData[AuthorIndex].split(":")[1],
                "accountid": AuthorsData[AuthorIndex].split(":")[0],
                "userid": AuthorsData[AuthorIndex].split(":")[2]
                },
            "id": LevelData[1],
            "downloads": LevelData[13],
            "likes": LevelData[19],
            "description": base64.b64decode(str(LevelData[35])).decode(),
            "original": LevelData[39],
            "difficulty": utils.GetDifficulty(LevelData),
            "length": utils.GetLength(LevelData[37])
            }
        
    except:
        return -1

    return LevelInfos

##################################################
##                                              ##
##  GET SONG INFORMATIONS                       ##
##  PARAMS: SONG ID                             ##
##                                              ##

def GetSongInfo(songid):
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "songID": str(songid),
        "secret": "Wmfd2893gb7"

    }
    Response = utils.SendRequest("getGJSongInfo", URLParameters)
    
    if Response == "-1":          
        return "-1"
    
    DataParser = recdata.split("~|~")
    
    SongInfos = {
        "name": DataParser[3],
        "id": DataParser[1],
        "author": DataParser[7],
        "size": DataParser[9] + "MB",
        }
        
    return SongInfos

##################################################
##                                              ##
##  GET DAILY INFORMATIONS                      ##
##  PARAMS: NONE                                ##
##                                              ##

def GetDailyLevel():
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "levelID": "-1",
        "secret": "Wmfd2893gb7"

    }
    Response = utils.SendHTTPRequest("downloadGJLevel22", URLParameters)
    
    LevelID = recdata.split(":")[1]    
    LevelInfos = GetLevelInfo(LevelID, "")
    
    return LevelInfos

###################################################
##                                               ##
##  GET WEEKLY INFORMATIONS                      ##
##  PARAMS: NONE                                 ##
##                                               ##

def GetWeeklyLevel():
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "levelID": "-2",
        "secret": "Wmfd2893gb7"

    }
    Response = utils.SendHTTPRequest("downloadGJLevel22", URLParameters)
    
    LevelID = recdata.split(":")[1]    
    LevelInfos = GetLevelInfo(LevelID, "")
    
    return LevelInfos

###################################################
##                                               ##
##  GET (PLAYERS) LEADERBOARDS INFORMATIONS      ##
##  PARAMS: PLAYERS COUNT                        ##
##                                               ##

def GetPlayersLeaderboard(str(PlayersCount)):
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "type": "top",
        "count": PlayersCount,
        "secret": "Wmfd2893gb7"

    }
    Response = utils.SendHTTPRequest("getGJScores20", URLParameters)

    if Response == "-1":          
        return -1
    
    UsersList = []    
    PlayersParser = Response.split("|")
    ReturnedPlayersCount = 0
    
    for i in data:
        PlayerInfos = i.split(":")

        try:
            StructureUser(PlayerInfos)               
            UsersList.append(user)
            ReturnedPlayersCount += 1
        except:
            pass
        
    return UsersList

###################################################
##                                               ##
##  GET (CREATORS) LEADERBOARDS INFORMATIONS     ##
##  PARAMS: PLAYERS COUNT                        ##
##                                               ##

def GetCreatorsLeaderboard(str(PlayersCount)):
    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "type": "creators",
        "count": PlayersCount,
        "secret": "Wmfd2893gb7"

    }
    Response = utils.SendHTTPRequest("getGJScores20", URLParameters)

    if Response == "-1":          
        return -1
    
    UsersList = []    
    PlayersParser = Response.split("|")
    ReturnedPlayersCount = 0
        
    for i in data:
        PlayerInfos = i.split(":")

        try:
            StructureUser(PlayerInfos)               
            UsersList.append(user)
            ReturnedPlayersCount += 1
        except:
            pass
        
    return UsersList

###################################################
##                                               ##
##  GET LEVELS LIST                              ##
##  PARAMS: PAGE - PARAM: TYPE                   ##
##  USED FOR FUNCTIONS LIKE GET(...)LEVELS       ##
##                                               ##

def GetLevelList(Page, Param_Type):
    Page = str(Page)
    Param_Type = str(Param_Type)

    URLParameters = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "len": "-",
        "type": Param_Type,
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": Page,
        "epic": "0",
        "secret": "Wmfd2893gb7"

    }
    Response = utils.SendHTTPRequest("getGJLevels21", URLParameters)
    
    if Response == "-1":         
        return -1
    
    LevelsList = []    
    LevelParser = Response.split("|")
    AuthorsData = Response.split("#")[1].split("|")
    AuthorIndex = 0
    
    for i in LevelParser:
        LevelData = i.split(":")
        try:
            for i in range(len(AuthorsData)):
                if AuthorsData[i].split(":")[0] == LevelData[7]:
                    AuthorIndex = i
                    break

            LevelInfo = {
                "name": LevelData[3],
                "author": {
                    "name": AuthorsData[AuthorIndex].split(":")[1],
                    "accountid": AuthorsData[AuthorIndex].split(":")[0],
                    "userid": AuthorsData[AuthorIndex].split(":")[2]
                    },
                "id": LevelData[1],
                "downloads": LevelData[13],
                "likes": LevelData[19],
                "description": base64.b64decode(str(LevelData[35])).decode(),
                "original": LevelData[39],
                "difficulty": utils.GetDifficulty(LevelData),
                "length": utils.GetLength(LevelData[37])
            }

            LevelsList.append(LevelInfo)
        except:
            pass

    return LevelsList

###################################################
##                                               ##
##  GET LEVELS LIST FUNCTIONS                    ##
##  PARAMS: PAGE                                 ##
##                                               ##

def GetFeaturedLevels(page):
    result = GetLevelList(page, 6)
    return result

def GetMostDownloadedLevels(page):
    result = GetLevelList(page, 1)
    return result

def GetTrending(page):
    result = GetLevelList(page, 3)
    return result

def GetRecentLevels(page):
    result = GetLevelList(page, 4)
    return result

def GetAwardedLevels(page):
    result = GetLevelList(page, 11)
    return result

def GetMagicLevels(page):
    result = GetLevelList(page, 7)
    return result
