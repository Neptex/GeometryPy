import GeometryPy.utils as utils
import base64

def GetUserInfo(accID, printbool):
    #Send HTTP request to get infos using accountID or username
    if not accID.isdigit():
        url = "http://www.boomlings.com/database/getGJUsers20.php"
        params = {
            "gameVersion": "21",
            "binaryVersion": "35",
            "gdw": "0",
            "str": str(accID),
            "secret": "Wmfd2893gb7"
        }
        parameters = utils.StructParams(params)    
        data = utils.SendRequest(url, parameters)
        accID = data.split(":")[21]

    url = "http://www.boomlings.com/database/getGJUserInfo20.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "targetAccountID": str(accID),
        "secret": "Wmfd2893gb7"
    }
    parameters = utils.StructParams(params)    
    data = utils.SendRequest(url, parameters)
    parser = data.split(":")

    user = {
        "username": parser[1],
        "stars": parser[13],
        "usercoins": parser[7],
        "demons": parser[17],
        "diamonds": parser[15],
        "youtube": parser[27],
        "twitter": "@"+parser[53],
        "twitch": parser[55],
        "accountid": parser[3],
        "userid": parser[49]
        }
    
    if printbool:
        print(user)
        
    return user

def GetLevelInfo(levelName, author, printbool):
    if author != "" and author != None:
        #Send HTTP request to get infos from author
        url = "http://www.boomlings.com/database/getGJUsers20.php"
        params = {
            "gameVersion": "21",
            "binaryVersion": "35",
            "str": str(author),
            "total": "0",
            "page": "0",
            "secret": "Wmfd2893gb7"

        }
        parameters = utils.StructParams(params)
        userdata = utils.SendRequest(url, parameters)

        #Use the accountID of the author to fetch the levels
        url = "http://www.boomlings.com/database/getGJLevels21.php"
        params = {
            "gameVersion": "21",
            "binaryVersion": "35",
            "gdw": "0",
            "str": str(userdata.split(":")[3]),
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
        parameters = utils.StructParams(params)  
        recdata = utils.SendRequest(url, parameters)
        levelparser = recdata.split("|")
        levelIndex = 0

        #Check for each levels if level name correspond to the researched one
        for i in range(len(levelparser)):
            parser = levelparser[i].split(":")
            if parser[3].lower() == levelName.lower():
                levelIndex = i
                break
            elif i == len(levelparser) - 1:
                levelIndex = -1
                break
    else:
        #Use the Level Name of the author to fetch the levels
        url = "http://www.boomlings.com/database/getGJLevels21.php"
        params = {
            "gameVersion": "21",
            "binaryVersion": "35",
            "gdw": "0",
            "str": str(levelName),
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
        parameters = utils.StructParams(params)  
        recdata = utils.SendRequest(url, parameters)
        levelparser = recdata.split("|")
        levelIndex = 0

    #Check if level found
    if levelIndex == -1:
        return utils.LEVEL_NOT_FOUND_ERROR
    else:
        authorIndex = 0
        data = levelparser[levelIndex].split(":")
        userdata = recdata.split("#")[1].split("|")
        for i in range(len(userdata)):
            if userdata[i].split(":")[0] == data[7]:
                authorIndex = i
                break

        if data[39] == "0":
            data[39] = "true"
            
        leveldata = {
            "name": data[3],
            "author": {
                "name": userdata[authorIndex].split(":")[1],
                "accountid": userdata[authorIndex].split(":")[0],
                "userid": userdata[authorIndex].split(":")[2]
                },
            "id": data[1],
            "downloads": data[13],
            "likes": data[19],
            "description": base64.b64decode(str(data[35])).decode(),
            "original": data[39],
            "difficulty": utils.GetDifficulty(data),
            "length": utils.GetLength(data[37])
            }
        
        if printbool:
            print(leveldata)

        return leveldata

def GetSongInfo(songid, printbool):
    url = "http://www.boomlings.com/database/getGJSongInfo.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "songID": str(songid),
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    data = recdata.split("~|~")
    
    song = {
        "name": data[3],
        "id": data[1],
        "author": data[7],
        "size": data[9] + "MB",
        }
        
    if printbool:
        print(song)
        
    return song

def GetDailyLevel(printbool): #Unfinished because abnormally not working
    url = "http://www.boomlings.com/database/downloadGJLevel22.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "levelID": "-1",
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    
    if printbool:
        print(recdata)
        
    return recdata

def GetWeeklyLevel(printbool): #Unfinished because abnormally not working
    url = "http://www.boomlings.com/database/downloadGJLevel22.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "levelID": "-2",
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    
    if printbool:
        print(recdata)
        
    return recdata    

def GetPlayersLeaderboard(playercount, printbool):
    url = "http://www.boomlings.com/database/getGJScores20.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "type": "top",
        "count": str(playercount),
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    data = recdata.split("|")
    UsersList = []
    
    for i in data:
        parser = i.split(":")

        try:
            user = {
                "username": parser[1],
                "stars": parser[23],
                "cp": parser[25],
                "usercoins": parser[7],
                "demons": parser[29],
                "diamonds": parser[27],
                "accountid": parser[3],
                "userid": parser[28]
                }                    
            UsersList.append(user)
        except:
            pass
        
    if printbool:
        print(UsersList)
        
    return UsersList

def GetCreatorsLeaderboard(playercount, printbool):
    url = "http://www.boomlings.com/database/getGJScores20.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "type": "creators",
        "count": str(playercount),
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    data = recdata.split("|")
    UsersList = []
    
    for i in data:
        parser = i.split(":")

        try:
            user = {
                "username": parser[1],
                "stars": parser[23],
                "cp": parser[25],
                "usercoins": parser[7],
                "demons": parser[29],
                "diamonds": parser[27],
                "accountid": parser[3],
                "userid": parser[28]
                }                    
            UsersList.append(user)
        except:
            pass
        
    if printbool:
        print(UsersList)
        
    return UsersList  

def GetFeaturedLevels(page, printbool):
    url = "http://www.boomlings.com/database/getGJLevels21.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "str": "",
        "len": "-",
        "type": "6",
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": str(page),
        "epic": "0",
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    levelparser = recdata.split("|")
    userdata = recdata.split("#")[1].split("|")
    LevelsList = []
    
    for i in levelparser:
        authorIndex = 0
        data = i.split(":")
        try:
            for i in range(len(userdata)):
                if userdata[i].split(":")[0] == data[7]:
                    authorIndex = i
                    break
                
            leveldata = {
                "name": data[3],
                "author": {
                    "name": userdata[authorIndex].split(":")[1],
                    "accountid": userdata[authorIndex].split(":")[0],
                    "userid": userdata[authorIndex].split(":")[2]
                    },
                "id": data[1],
                "downloads": data[13],
                "likes": data[19],
                "description": base64.b64decode(str(data[35])).decode(),
                "original": data[39],
                "difficulty": utils.GetDifficulty(data),
                "length": utils.GetLength(data[37])
            }


            LevelsList.append(leveldata)
        except:
            pass
        
    if printbool:
        print(LevelsList)
                    
    return LevelsList

def GetMostDownloadedLevels(page, printbool):
    url = "http://www.boomlings.com/database/getGJLevels21.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "str": "",
        "len": "-",
        "type": "1",
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": str(page),
        "epic": "0",
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    levelparser = recdata.split("|")
    userdata = recdata.split("#")[1].split("|")
    LevelsList = []
    
    for i in levelparser:
        authorIndex = 0
        data = i.split(":")
        try:
            for i in range(len(userdata)):
                if userdata[i].split(":")[0] == data[7]:
                    authorIndex = i
                    break
                
            leveldata = {
                "name": data[3],
                "author": {
                    "name": userdata[authorIndex].split(":")[1],
                    "accountid": userdata[authorIndex].split(":")[0],
                    "userid": userdata[authorIndex].split(":")[2]
                    },
                "id": data[1],
                "downloads": data[13],
                "likes": data[19],
                "description": base64.b64decode(str(data[35])).decode(),
                "original": data[39],
                "difficulty": utils.GetDifficulty(data),
                "length": utils.GetLength(data[37])
            }


            LevelsList.append(leveldata)
        except:
            pass
        
    if printbool:
        print(LevelsList)
                    
    return LevelsList

def GetTrending(page, printbool):
    url = "http://www.boomlings.com/database/getGJLevels21.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "str": "",
        "len": "-",
        "type": "3",
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": str(page),
        "epic": "0",
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    levelparser = recdata.split("|")
    userdata = recdata.split("#")[1].split("|")
    LevelsList = []
    
    for i in levelparser:
        authorIndex = 0
        data = i.split(":")
        try:
            for i in range(len(userdata)):
                if userdata[i].split(":")[0] == data[7]:
                    authorIndex = i
                    break
                
            leveldata = {
                "name": data[3],
                "author": {
                    "name": userdata[authorIndex].split(":")[1],
                    "accountid": userdata[authorIndex].split(":")[0],
                    "userid": userdata[authorIndex].split(":")[2]
                    },
                "id": data[1],
                "downloads": data[13],
                "likes": data[19],
                "description": base64.b64decode(str(data[35])).decode(),
                "original": data[39],
                "difficulty": utils.GetDifficulty(data),
                "length": utils.GetLength(data[37])
            }


            LevelsList.append(leveldata)
        except:
            pass
        
    if printbool:
        print(LevelsList)
                    
    return LevelsList

def GetRecentLevels(page, printbool):
    url = "http://www.boomlings.com/database/getGJLevels21.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "str": "",
        "len": "-",
        "type": "4",
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": str(page),
        "epic": "0",
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    levelparser = recdata.split("|")
    userdata = recdata.split("#")[1].split("|")
    LevelsList = []
    
    for i in levelparser:
        authorIndex = 0
        data = i.split(":")
        try:
            for i in range(len(userdata)):
                if userdata[i].split(":")[0] == data[7]:
                    authorIndex = i
                    break
                
            leveldata = {
                "name": data[3],
                "author": {
                    "name": userdata[authorIndex].split(":")[1],
                    "accountid": userdata[authorIndex].split(":")[0],
                    "userid": userdata[authorIndex].split(":")[2]
                    },
                "id": data[1],
                "downloads": data[13],
                "likes": data[19],
                "description": base64.b64decode(str(data[35])).decode(),
                "original": data[39],
                "difficulty": utils.GetDifficulty(data),
                "length": utils.GetLength(data[37])
            }


            LevelsList.append(leveldata)
        except:
            pass
        
    if printbool:
        print(LevelsList)
                    
    return LevelsList

def GetAwardedLevels(page, printbool):
    url = "http://www.boomlings.com/database/getGJLevels21.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "str": "",
        "len": "-",
        "type": "11",
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": str(page),
        "epic": "0",
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    levelparser = recdata.split("|")
    userdata = recdata.split("#")[1].split("|")
    LevelsList = []
    
    for i in levelparser:
        authorIndex = 0
        data = i.split(":")
        try:
            for i in range(len(userdata)):
                if userdata[i].split(":")[0] == data[7]:
                    authorIndex = i
                    break
                
            leveldata = {
                "name": data[3],
                "author": {
                    "name": userdata[authorIndex].split(":")[1],
                    "accountid": userdata[authorIndex].split(":")[0],
                    "userid": userdata[authorIndex].split(":")[2]
                    },
                "id": data[1],
                "downloads": data[13],
                "likes": data[19],
                "description": base64.b64decode(str(data[35])).decode(),
                "original": data[39],
                "difficulty": utils.GetDifficulty(data),
                "length": utils.GetLength(data[37])
            }


            LevelsList.append(leveldata)
        except:
            pass
        
    if printbool:
        print(LevelsList)
                    
    return LevelsList

def GetMagicLevels(page, printbool):
    url = "http://www.boomlings.com/database/getGJLevels21.php"
    params = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "str": "",
        "len": "-",
        "type": "7",
        "diff": "-",
        "featured": "0",
        "original": "0",
        "twoPlayer": "0",
        "coins": "0",
        "page": str(page),
        "epic": "0",
        "secret": "Wmfd2893gb7"

    }
    parameters = utils.StructParams(params)  
    recdata = utils.SendRequest(url, parameters)
    levelparser = recdata.split("|")
    userdata = recdata.split("#")[1].split("|")
    LevelsList = []
    
    for i in levelparser:
        authorIndex = 0
        data = i.split(":")
        try:
            for i in range(len(userdata)):
                if userdata[i].split(":")[0] == data[7]:
                    authorIndex = i
                    break
                
            leveldata = {
                "name": data[3],
                "author": {
                    "name": userdata[authorIndex].split(":")[1],
                    "accountid": userdata[authorIndex].split(":")[0],
                    "userid": userdata[authorIndex].split(":")[2]
                    },
                "id": data[1],
                "downloads": data[13],
                "likes": data[19],
                "description": base64.b64decode(str(data[35])).decode(),
                "original": data[39],
                "difficulty": utils.GetDifficulty(data),
                "length": utils.GetLength(data[37])
            }


            LevelsList.append(leveldata)
        except:
            pass
        
    if printbool:
        print(LevelsList)
                    
    return LevelsList
