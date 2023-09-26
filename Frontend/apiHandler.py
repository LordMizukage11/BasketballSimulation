import requests
from player import Player  # Import the Player class from player.py

class ApiHandler:
    def __init__(self):
        self.URLGetPlayer = "http://192.168.4.47:3100/api/players"
        self.URLNewPlayer ="http://192.168.4.47:3100/api/newplayer"
        self.headers = {"Content-Type": "application/json"}
    
    def createPlayer(self, firstName, lastName, age, height, weight, strength, endurance, agility, speed, iq, jump, dribble, passing, layup, midrange, three, steal, rebound, insideD, outsideD):
        # Define the player data as a dictionary
        playerData = {
            "firstName": firstName,
            "lastName": lastName,
            "age": age,
            "height": height,
            "weight": weight,
            "strength": strength,
            "endurance": endurance,
            "agility": agility,
            "speed": speed,
            "iq": iq,
            "jump": jump,
            "dribble": dribble,
            "pass": passing,
            "layup": layup,
            "midrange": midrange,
            "three": three,
            "steal": steal,
            "rebound": rebound,
            "insideD": insideD,
            "outsideD": outsideD
        }

        # Send a POST request to create a new player
        response = requests.post(self.URLNewPlayer, headers=self.headers, json=playerData)

        if response.status_code == 201:
            print("Player created successfully!")
        else:
            print("Failed to create a new player. Status code:", response.status_code)
            
            
    def getPlayer(self, fullName):
        params = {"fullName": fullName}
        response = requests.get(self.URLGetPlayer, headers=self.headers, params=params)
        
        if response.status_code == 200:
            print("Player found!")
            playerDataList = response.json()

            if isinstance(playerDataList, list) and len(playerDataList) > 0:
                # Assuming the first item in the list is the player of interest
                playerData = playerDataList[0]

                # Extract relevant fields from the player data
                firstName = playerData.get("FirstName", "")
                lastName = playerData.get("LastName", "")
                age = playerData.get("Age", 0)
                height = playerData.get("Height", 0)
                weight = playerData.get("Weight", 0)
                strength = playerData.get("Strength", 0)
                endurance = playerData.get("Endurance", 0)
                agility = playerData.get("Agility", 0)
                speed = playerData.get("Speed", 0)
                iq = playerData.get("IQ", 0)
                jump = playerData.get("Jump", 0)
                dribble = playerData.get("Dribble", 0)
                passing = playerData.get("Pass", 0)
                layup = playerData.get("Layup", 0)
                midrange = playerData.get("Midrange", 0)
                three = playerData.get("Three", 0)
                steal = playerData.get("Steal", 0)
                rebound = playerData.get("Rebound", 0)
                insideD = playerData.get("InsideD", 0)
                outsideD = playerData.get("OutsideD", 0)
                hot = playerData.get("Hot", False)
                temperature = playerData.get("Temperature", 0)
                traits = playerData.get("Traits", "")

                # Create a Player instance using the extracted data
                player = Player(
                    firstName, lastName, fullName, age, height, weight,
                    strength, endurance, agility, speed, iq, jump, dribble,
                    passing, layup, midrange, three, steal, rebound, insideD,
                    outsideD, hot, temperature, traits
                )

                return player
            else:
                print("No player data found in the list.")
                return None
        else:
            print("Player not found!")
            return None


