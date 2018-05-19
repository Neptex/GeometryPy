import urllib.request
from urllib.request import urlopen, Request
import GeometryPy.commands as GDPyCommands

def GetUserInfo(accID):
    result = GDPyCommands.GetUserInfo(accID)
    return result

def GetLevelInfo(lvlname, author=""):
    result = GDPyCommands.GetLevelInfo(lvlname, author)
    return result

def GetSongInfo(songid):
    result = GDPyCommands.GetSongInfo(songid)
    return result

def GetDailyLevel():
    result = GDPyCommands.GetDailyLevel()
    return result

def GetWeeklyLevel():
    result = GDPyCommands.GetWeeklyLevel()
    return result

def GetPlayersLeaderboard(playercount):
    result = GDPyCommands.GetPlayersLeaderboard(playercount)
    return result

def GetCreatorsLeaderboard(playercount):
    result = GDPyCommands.GetCreatorsLeaderboard(playercount)
    return result

def GetFeaturedLevels(page):
    result = GDPyCommands.GetFeaturedLevels(page)
    return result

def GetMostDownloadedLevels(page):
    result = GDPyCommands.GetMostDownloadedLevels(page)
    return result

def GetMostLikedLevels(page):
    result = GDPyCommands.GetMostLikedLevels(page)
    return result    

def GetTrending(page):
    result = GDPyCommands.GetTrending(page)
    return result

def GetRecentLevels(page):
    result = GDPyCommands.GetRecentLevels(page)
    return result

def GetAwardedLevels(page):
    result = GDPyCommands.GetAwardedLevels(page)
    return result

def GetMagicLevels(page):
    result = GDPyCommands.GetMagicLevels(page)
    return result
