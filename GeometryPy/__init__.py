import urllib.request
from urllib.request import urlopen, Request
import GeometryPy.commands as GDPyCommands

PrintReturn = False

def GetUserInfo(accID):
    result = GDPyCommands.GetUserInfo(accID, PrintReturn)
    return result

def GetLevelInfo(lvlname, author=""):
    result = GDPyCommands.GetLevelInfo(lvlname, author, PrintReturn)
    return result

def GetSongInfo(songid):
    result = GDPyCommands.GetSongInfo(songid, PrintReturn)
    return result

#def GetDailyLevel():
#    result = GDPyCommands.GetDailyLevel(PrintReturn)
#    return result

#def GetWeeklyLevel():
#    result = GDPyCommands.GetWeeklyLevel(PrintReturn)
#    return result

def GetPlayersLeaderboard(playercount):
    result = GDPyCommands.GetPlayersLeaderboard(playercount, PrintReturn)
    return result

def GetCreatorsLeaderboard(playercount):
    result = GDPyCommands.GetCreatorsLeaderboard(playercount, PrintReturn)
    return result

def GetFeaturedLevels(page):
    result = GDPyCommands.GetFeaturedLevels(page, PrintReturn)
    return result

def GetMostDownloadedLevels(page):
    result = GDPyCommands.GetMostDownloadedLevels(page, PrintReturn)
    return result

def GetMostLikedLevels(page):
    result = GDPyCommands.GetMostLikedLevels(page, PrintReturn)
    return result    

def GetTrending(page):
    result = GDPyCommands.GetTrending(page, PrintReturn)
    return result

def GetRecentLevels(page):
    result = GDPyCommands.GetRecentLevels(page, PrintReturn)
    return result

def GetAwardedLevels(page):
    result = GDPyCommands.GetAwardedLevels(page, PrintReturn)
    return result

def GetMagicLevels(page):
    result = GDPyCommands.GetMagicLevels(page, PrintReturn)
    return result
