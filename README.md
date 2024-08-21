#
<div align="center">
  <br />
  <p>
    <a><img src="https://i.ibb.co/2shXHs5/logo-GEOMETRY-pu.png" width="546" alt="GeometryPy" /></a>
  </p>
  <br />
  <p>
</div>

<b>/!\ Only works for 2.1 /!\

# Installation
You can install the library here https://github.com/NerexGD/GeometryPy/releases/ but you can also download it by clicking the green button "Clone or Download". Extract GeometryPy from the .zip and add it to your project directory. You're ready to go!
# Usage
GeometryPy have a lot of features: Get user stats, Get level info, Get featured levels, and more!

Get started by importing the package to your project
```Python
import GeometryPy
or
import GeometryPy as GDClient
or
import GeometryPy as [insert what you want here]
#Because i know we're sometimes lazy to write a long word
```

You can now start to use GeometryPy! Enjoy!

# Functions
| Function | Parameters | Result |
|------|------|------------|
| GetUserInfo | AccountID or Username | Returns a dict which contains informations about an **User** |
| GetLevelInfo | Level Name or LevelID, *Creator (optional)* | Returns a dict which contains informations about a **Level**
| GetSongInfo | SongID | Returns a dict which contains informations about a **Song** |
| GetPlayersLeaderboard | Players Amount | Returns a list which contains multiples dicts with **top players stats** |
| GetCreatorsLeaderboard | Players Amount | Returns a list which contains multiples dicts with **top creators stats** |
| GetFeaturedLevels | Page | Returns a list which contains multiples dicts with **featured levels info** |
| GetMostDownloadedLevels | Page | Returns a list which contains multiples dicts with **most downloaded levels info** |
| GetMostLikedLevels | Page | Returns a list which contains multiples dicts with **most liked levels info** |
| GetRecentLevels | Page | Returns a list which contains multiples dicts with **recents levels info** |
| GetAwardedLevels | Page | Returns a list which contains multiples dicts with **awarded levels info** |
| GetMagicLevels | Page | Returns a list which contains multiples dicts with **magics levels info** |

# Example
In this example, you can get stats of the user "Nerex", Get infos of the level "Cataclysm" but also get the top 100 creators leaderboard!
```Python
import GeometryPy as GDClient

Player = GDClient.GetUserInfo("Nerex") #You can also use an AccountID!
print(Player) 

""" returns: { 'username': 'Nerex', 
                       'stars': '1340', 
                       'usercoins': '130', 
                       'demons': '40', 
                       'diamonds': '1919',
                       'cp': '2',
                       'youtube': 'UC5JsIMU43qQw9ggxdVpJgRg', 
                       'twitter': '@Nerex1', 
                       'twitch': 'NerexGD', 
                       'accountid': '20207462', 
                       'userid': '5837301' } 
"""        
                       
print(Player["username"]) # returns "Nerex"


Level = GDClient.GetLevelInfo("Cataclysm") #You can also use a Level ID and specify a creator! (GDClient.GetLevelInfo("Cataclysm", "GgBoy")
print(Level["stars"]) # return 10


LeaderboardCreators = GDClient.GetCreatorsLeaderboard(100)
print(LeaderboardCreators[0]) # returns ViPrIn
```
