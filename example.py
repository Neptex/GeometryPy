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
print(LeaderboardCreators[0]["username"]) # returns ViPrIn
