import GeometryPy as GDClient

data = GDClient.GetUserInfo("Nerex")

print(data) # returns { 'username': 'Nerex', 
                       'stars': '1340', 
                       'usercoins': '130', 
                       'demons': '40', 
                       'diamonds': '1919', 
                       'youtube': 'UC5JsIMU43qQw9ggxdVpJgRg', 
                       'twitter': '@Nerex1', 
                       'twitch': 'NerexGD', 
                       'accountid': '20207462', 
                       'userid': '5837301' }

                
print(data["username"]) #returns "Nerex"
